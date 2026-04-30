import streamlit as st
import pyabf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, optimize, integrate
import tempfile
import os
import pandas as pd

# --- CONFIGURATION ---
st.set_page_config(page_title="sEPSC Pipeline", layout="wide")

# --- LANGUAGE SELECTION ---
lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])

# Translation Dictionary
T = {
    "English": {
        "title": "# sEPSC Expert Pipeline: Denoising, Kinetics & Export",
        "branding": "Manzoni Lab - Branding",
        "sb_bessel": "1. Bessel Filter (Denoising)",
        "activate_bessel": "Enable Bessel",
        "sb_detec": "2. Multi-Scale Detection",
        "threshold": "Z-Score Threshold",
        "sb_kinetics": "3. Kinetics & Filters",
        "calc_raw": "Calculate on RAW trace",
        "amp_filter": "Amplitude Filter (>7pA)",
        "decay_filter": "Decay Filter (<4ms)",
        "sb_viz": "4. Visualization",
        "zoom_y": "Zoom Y (pA)",
        "zoom_x": "Zoom X (s)",
        "uploader": "Upload .abf",
        "viz_header": "Visualization & Detection",
        "export_header": "📥 Export Results",
        "btn_events": "📁 Download Individual Events (CSV)",
        "btn_summary": "📊 Download Population Analysis & Distributions (CSV)",
        "stats_header": "Population Means",
        "dist_header": "Distributions",
        "col_time": "Time (s)",
        "col_amp": "Amplitude (pA)",
        "col_rise": "Rise Time 10-90% (ms)",
        "col_area": "Area (pA.ms)",
        "col_iei": "IEI (ms)",
        "metric_count": "Event Count",
        "metric_freq": "Frequency (Hz)",
        "metric_iei": "Mean IEI (ms)",
        "metric_amp": "Mean Amplitude (pA)",
        "metric_rise": "Mean Rise Time (ms)",
        "metric_area": "Mean Area (pA.ms)"
    },
    "Français": {
        "title": "# Pipeline Expert sEPSC : Denoising, Cinétique & Exportation",
        "branding": "Manzoni Lab - Branding",
        "sb_bessel": "1. Filtre Bessel (Denoising)",
        "activate_bessel": "Activer Bessel",
        "sb_detec": "2. Détection Multi-Scale",
        "threshold": "Seuil Z-Score",
        "sb_kinetics": "3. Cinétique & Filtres",
        "calc_raw": "Calculer sur trace BRUTE",
        "amp_filter": "Filtre Amplitude (>7pA)",
        "decay_filter": "Filtre Decay (<4ms)",
        "sb_viz": "4. Visualisation",
        "zoom_y": "Zoom Y (pA)",
        "zoom_x": "Zoom X (s)",
        "uploader": "Charger .abf",
        "viz_header": "Visualisation & Détection",
        "export_header": "📥 Exportation des Résultats",
        "btn_events": "📁 Télécharger Événements Individuels (CSV)",
        "btn_summary": "📊 Télécharger Analyse Population & Distributions (CSV)",
        "stats_header": "Moyennes de Population",
        "dist_header": "Distributions",
        "col_time": "Temps (s)",
        "col_amp": "Amplitude (pA)",
        "col_rise": "Rise Time 10-90% (ms)",
        "col_area": "Aire (pA.ms)",
        "col_iei": "IEI (ms)",
        "metric_count": "Nombre d'événements",
        "metric_freq": "Fréquence (Hz)",
        "metric_iei": "IEI Moyen (ms)",
        "metric_amp": "Amplitude Moyenne (pA)",
        "metric_rise": "Rise Time Moyen (ms)",
        "metric_area": "Aire Moyenne (pA.ms)"
    }
}[lang]

# --- EN-TÊTE INSTITUTIONNEL ---
col_l, col_r = st.columns([2, 5]) 
with col_l:
    try: st.image("logo_chavis_final.png", width=360) 
    except: st.info(T["branding"]) 
with col_r:
    st.markdown(T["title"])

# --- FONCTIONS DE CALCUL EXPERT ---
def apply_bessel_filter(data, fs, cutoff=2000, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.bessel(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, data)

def get_precise_time(times, values, target):
    for i in range(len(values)-1, 0, -1):
        if values[i] >= target > values[i-1]:
            t1, t2 = times[i-1], times[i]
            y1, y2 = values[i-1], values[i]
            return t1 + (target - y1) * (t2 - t1) / (y2 - y1)
    return times[np.where(values >= target)[0][0]]

def calculate_rise_time_expert(segment_y, dt):
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

# --- SIDEBAR ---
st.sidebar.header(T["sb_bessel"])
use_bessel = st.sidebar.checkbox(T["activate_bessel"], value=True)
cutoff = st.sidebar.slider("Cutoff (Hz)", 500, 5000, 2000)

st.sidebar.header(T["sb_detec"])
threshold = st.sidebar.slider(T["threshold"], 1.0, 8.0, 2.5)
default_decays = [2.0, 5.0, 10.0, 15.0]

st.sidebar.header(T["sb_kinetics"])
calc_on_raw = st.sidebar.checkbox(T["calc_raw"], value=False)
use_amp_filter = st.sidebar.checkbox(T["amp_filter"], value=True)
use_decay_filter = st.sidebar.checkbox(T["decay_filter"], value=False)

st.sidebar.header(T["sb_viz"])
y_zoom = st.sidebar.slider(T["zoom_y"], -300, 100, (-80, 20))
x_zoom = st.sidebar.slider(T["zoom_x"], 0.0, 600.0, (0.0, 2.0), step=0.1)

# --- MAIN LOGIC ---
file = st.file_uploader(T["uploader"], type=["abf"])

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

        st.subheader(T["viz_header"])
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
            duration_sec = times[-1]
            freq_hz = len(df) / duration_sec
            mean_iei_ms = df['iei'].mean()
            n_bins = 25
            counts_amp, bins_amp = np.histogram(df['amp'], bins=n_bins)
            counts_rise, bins_rise = np.histogram(df['rise'], bins=n_bins)
            iei_clean = df['iei'].dropna()
            counts_iei, bins_iei = np.histogram(iei_clean, bins=n_bins) if not iei_clean.empty else (np.zeros(n_bins), np.zeros(n_bins+1))

            # Export formatting
            df_export_events = df[['time', 'amp', 'rise', 'area', 'iei']].copy()
            df_export_events.rename(columns={'time': T['col_time'], 'amp': T['col_amp'], 'rise': T['col_rise'], 'area': T['col_area'], 'iei': T['col_iei']}, inplace=True)
            
            metrics_keys = [T['metric_count'], T['metric_freq'], T['metric_iei'], T['metric_amp'], T['metric_rise'], T['metric_area']]
            metrics_vals = [len(df), freq_hz, mean_iei_ms, df['amp'].mean(), df['rise'].mean(), df['area'].mean()]
            pad_len = n_bins - len(metrics_keys)
            metrics_keys += [np.nan] * pad_len
            metrics_vals += [np.nan] * pad_len

            df_export_summary = pd.DataFrame({
                'Global_Metric': metrics_keys, 'Global_Value': metrics_vals,
                'Amp_Bin_Center': (bins_amp[:-1] + bins_amp[1:]) / 2, 'Amp_Counts': counts_amp,
                'Rise_Bin_Center': (bins_rise[:-1] + bins_rise[1:]) / 2, 'Rise_Counts': counts_rise,
                'IEI_Bin_Center': (bins_iei[:-1] + bins_iei[1:]) / 2, 'IEI_Counts': counts_iei
            })

            st.subheader(T["export_header"])
            col_exp1, col_exp2 = st.columns(2)
            col_exp1.download_button(label=T["btn_events"], data=df_export_events.to_csv(index=False).encode('utf-8'), file_name='sEPSC_events.csv', mime='text/csv')
            col_exp2.download_button(label=T["btn_summary"], data=df_export_summary.to_csv(index=False).encode('utf-8'), file_name='sEPSC_population.csv', mime='text/csv')

            st.divider()
            st.subheader(T["stats_header"])
            c1, c2, c3, c4 = st.columns(4)
            c1.metric(T["col_amp"], f"{df['amp'].mean():.2f} pA")
            c2.metric(T["metric_freq"], f"{freq_hz:.2f} Hz")
            c3.metric(T["metric_iei"], f"{mean_iei_ms:.2f} ms")
            c4.metric(T["col_area"], f"{df['area'].mean():.2f} pA.ms")

            st.subheader(T["dist_header"])
            fig2, (ha, hb, hc) = plt.subplots(1, 3, figsize=(15, 4))
            ha.bar((bins_amp[:-1] + bins_amp[1:]) / 2, counts_amp, width=(bins_amp[1]-bins_amp[0])*0.9, color='gray')
            ha.set_title(T["col_amp"])
            hb.bar((bins_rise[:-1] + bins_rise[1:]) / 2, counts_rise, width=(bins_rise[1]-bins_rise[0])*0.9, color='#FF8C00')
            hb.set_title(T["col_rise"])
            hc.bar((bins_iei[:-1] + bins_iei[1:]) / 2, counts_iei, width=(bins_iei[1]-bins_iei[0])*0.9, color='salmon')
            hc.set_title(T["col_iei"])
            st.pyplot(fig2)

    except Exception as e: st.error(f"Error: {e}")
    finally:
        if os.path.exists(tmp_path): os.remove(tmp_path)
