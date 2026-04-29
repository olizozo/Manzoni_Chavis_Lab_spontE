import streamlit as st
import pyabf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, optimize, integrate
import tempfile
import os
import pandas as pd

# --- FONCTIONS DE CALCUL EXPERT ---

def apply_bessel_filter(data, fs, cutoff=2000, order=4):
    """Filtre de Bessel d'ordre 4 : Phase linéaire pour préserver le Rise Time."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.bessel(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, data)

def get_precise_time(times, values, target):
    """Cherche le temps exact d'un seuil en remontant depuis le pic."""
    for i in range(len(values)-1, 0, -1):
        if values[i] >= target > values[i-1]:
            t1, t2 = times[i-1], times[i]
            y1, y2 = values[i-1], values[i]
            return t1 + (target - y1) * (t2 - t1) / (y2 - y1)
    return times[np.where(values >= target)[0][0]]

def calculate_rise_time_expert(segment_y, dt):
    """Calcule le Rise Time 10-90% avec recherche inversée et interpolation."""
    try:
        peak_idx = np.argmax(segment_y)
        if peak_idx < 3: return 0
        
        rising_limb = segment_y[:peak_idx + 1]
        t_vec = np.arange(len(rising_limb)) * dt
        
        peak_val = rising_limb[-1]
        y10, y90 = 0.10 * peak_val, 0.90 * peak_val
        
        t10 = get_precise_time(t_vec, rising_limb, y10)
        t90 = get_precise_time(t_vec, rising_limb, y90)
        
        return t90 - t10
    except: return 0

# --- INTERFACE ---
st.set_page_config(layout="wide", page_title="sEPSC Pipeline")
st.title("🔬 Pipeline Expert sEPSC : Denoising, Cinétique & Exportation")

# --- SIDEBAR ---
st.sidebar.header("1. Bessel Filter (Denoising)")
use_bessel = st.sidebar.checkbox("Activer Bessel", value=True)
cutoff = st.sidebar.slider("Cutoff (Hz)", 500, 5000, 2000)

st.sidebar.header("2. Détection Multi-Scale")
threshold = st.sidebar.slider("Seuil Z-Score", 1.0, 8.0, 2.5)
default_decays = [2.0, 5.0, 10.0, 15.0]

st.sidebar.header("3. Cinétique & Filtres")
calc_on_raw = st.sidebar.checkbox("Calculer sur trace BRUTE", value=False)
use_amp_filter = st.sidebar.checkbox("Filtre Amplitude (>7pA)", value=True)
use_decay_filter = st.sidebar.checkbox("Filtre Decay (<4ms)", value=False)

st.sidebar.header("4. Visualisation")
y_zoom = st.sidebar.slider("Zoom Y (pA)", -300, 100, (-80, 20))
x_zoom = st.sidebar.slider("Zoom X (s)", 0.0, 600.0, (0.0, 2.0), step=0.1)

# --- LOGIQUE PRINCIPALE ---
file = st.file_uploader("Charger .abf", type=["abf"])

if file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.abf') as tmp:
        tmp.write(file.getvalue())
        tmp_path = tmp.name

    try:
        abf = pyabf.ABF(tmp_path)
        abf.setSweep(0)
        fs, times, dt = abf.dataRate, abf.sweepX, 1000/abf.dataRate
        raw_data = abf.sweepY - np.median(abf.sweepY)
        
        f_data = apply_bessel_filter(raw_data, fs, cutoff) if use_bessel else raw_data
        
        best_corr = np.zeros_like(f_data)
        for d in default_decays:
            t_tmpl = np.arange(0, 20, dt)
            tmpl = (np.exp(-t_tmpl/d) - np.exp(-t_tmpl/0.5))
            tmpl /= np.max(np.abs(tmpl))
            best_corr = np.maximum(best_corr, signal.correlate(-f_data, tmpl, mode='same'))
        
        corr_z = (best_corr - np.mean(best_corr)) / np.std(best_corr)
        peaks, _ = signal.find_peaks(corr_z, height=threshold, distance=int(0.005 * fs))
        
        valid_ev = []
        k_trace = raw_data if calc_on_raw else f_data
        
        for i, p in enumerate(peaks):
            start, end = p - int(0.003*fs), p + int(0.015*fs)
            if start < 0 or end >= len(k_trace): continue
            
            l_base = np.mean(k_trace[p-int(0.005*fs):p-int(0.002*fs)])
            seg_inv = -(k_trace[start:end] - l_base)
            
            amp = np.max(seg_inv)
            rise_1090 = calculate_rise_time_expert(seg_inv, dt)
            area = integrate.trapezoid(seg_inv, dx=dt)
            
            if (not use_amp_filter or amp >= 7):
                ev = {'idx': p, 'time': times[p], 'amp': amp, 'rise': rise_1090, 'area': area}
                ev['iei'] = (times[p] - times[peaks[i-1]])*1000 if i>0 else np.nan
                valid_ev.append(ev)

        # --- AFFICHAGE ---
        st.subheader("Visualisation & Détection")
        fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios':[2,1]})
        ax1.plot(times, f_data, color='black', lw=0.4)
        if valid_ev: ax1.plot([e['time'] for e in valid_ev], [f_data[e['idx']] for e in valid_ev], 'o', color='#FF8C00', markersize=5)
        ax1.set_ylim(y_zoom); ax1.set_xlim(x_zoom)
        ax2.plot(times, corr_z, color='blue', alpha=0.5)
        ax2.axhline(threshold, color='red', ls='--')
        st.pyplot(fig1)

        if valid_ev:
            df = pd.DataFrame(valid_ev)
            st.divider()
            
            # --- CALCULS STATISTIQUES ET DISTRIBUTIONS ---
            duration_sec = times[-1]
            freq_hz = len(df) / duration_sec
            mean_iei_ms = df['iei'].mean()
            
            # Histogrammes pour l'export (25 Bins)
            n_bins = 25
            counts_amp, bins_amp = np.histogram(df['amp'], bins=n_bins)
            counts_rise, bins_rise = np.histogram(df['rise'], bins=n_bins)
            
            iei_clean = df['iei'].dropna()
            if not iei_clean.empty:
                counts_iei, bins_iei = np.histogram(iei_clean, bins=n_bins)
            else:
                counts_iei, bins_iei = np.zeros(n_bins), np.zeros(n_bins+1)

            # --- Création des DataFrames pour Exportation ---
            # 1. Données individuelles
            df_export_events = df[['time', 'amp', 'rise', 'area', 'iei']].copy()
            df_export_events.rename(columns={'time': 'Temps (s)', 'amp': 'Amplitude (pA)', 'rise': 'Rise Time 10-90% (ms)', 'area': 'Aire (pA.ms)', 'iei': 'IEI (ms)'}, inplace=True)
            
            # 2. Données de population avec distributions intégrées
            metrics_keys = ["Nombre d'événements", "Fréquence (Hz)", "IEI Moyen (ms)", "Amplitude Moyenne (pA)", "Rise Time Moyen (ms)", "Aire Moyenne (pA.ms)"]
            metrics_vals = [len(df), freq_hz, mean_iei_ms, df['amp'].mean(), df['rise'].mean(), df['area'].mean()]
            
            # Padding avec NaN pour égaliser la longueur du DataFrame (n_bins lignes)
            pad_len = n_bins - len(metrics_keys)
            metrics_keys += [np.nan] * pad_len
            metrics_vals += [np.nan] * pad_len

            df_export_summary = pd.DataFrame({
                'Metrique_Globale': metrics_keys,
                'Valeur_Globale': metrics_vals,
                'Amp_Bin_Center (pA)': (bins_amp[:-1] + bins_amp[1:]) / 2,
                'Amp_Counts': counts_amp,
                'Rise_Bin_Center (ms)': (bins_rise[:-1] + bins_rise[1:]) / 2,
                'Rise_Counts': counts_rise,
                'IEI_Bin_Center (ms)': (bins_iei[:-1] + bins_iei[1:]) / 2,
                'IEI_Counts': counts_iei
            })

            # --- Exportation CSV (Interface) ---
            st.subheader("📥 Exportation des Résultats")
            col_exp1, col_exp2 = st.columns(2)
            
            csv_events = df_export_events.to_csv(index=False).encode('utf-8')
            col_exp1.download_button(
                label="📁 Télécharger Événements Individuels (CSV)",
                data=csv_events,
                file_name='sEPSC_evenements_individuels.csv',
                mime='text/csv',
            )

            csv_summary = df_export_summary.to_csv(index=False).encode('utf-8')
            col_exp2.download_button(
                label="📊 Télécharger Analyse Population & Distributions (CSV)",
                data=csv_summary,
                file_name='sEPSC_analyse_population_distributions.csv',
                mime='text/csv',
            )

            st.divider()

            # Stats à l'écran
            st.subheader("Moyennes de Population")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Amplitude", f"{df['amp'].mean():.2f} pA")
            c2.metric("Fréquence", f"{freq_hz:.2f} Hz")
            c3.metric("IEI Moyen", f"{mean_iei_ms:.2f} ms")
            c4.metric("Aire (Charge)", f"{df['area'].mean():.2f} pA.ms")

            st.subheader("Distributions")
            fig2, (ha, hb, hc) = plt.subplots(1, 3, figsize=(15, 4))
            ha.bar((bins_amp[:-1] + bins_amp[1:]) / 2, counts_amp, width=(bins_amp[1]-bins_amp[0])*0.9, color='gray')
            ha.set_title("Amplitude (pA)")
            
            hb.bar((bins_rise[:-1] + bins_rise[1:]) / 2, counts_rise, width=(bins_rise[1]-bins_rise[0])*0.9, color='#FF8C00')
            hb.set_title("Rise Time 10-90% (ms)")
            
            hc.bar((bins_iei[:-1] + bins_iei[1:]) / 2, counts_iei, width=(bins_iei[1]-bins_iei[0])*0.9, color='salmon')
            hc.set_title("IEI (ms)")
            st.pyplot(fig2)

    except Exception as e: st.error(f"Erreur : {e}")
    finally:
        if os.path.exists(tmp_path): os.remove(tmp_path)