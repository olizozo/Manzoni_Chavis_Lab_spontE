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

# --- INITIALISATION ---
if 'fs_nyquist' not in st.session_state:
    st.session_state.fs_nyquist = 5000.0

# --- LANGUAGE SELECTION ---
lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])

T = {
    "English": {
        "title": "# sEPSC Expert Pipeline: Denoising, Kinetics & Export",
        "sb_bessel": "1. Bessel Filter (Denoising)",
        "cutoff": "Cutoff (Hz)",
        "nyquist_warn": "⚠️ Limited by Nyquist frequency",
        "sb_detec": "2. Multi-Scale Detection",
        "threshold": "Z-Score Threshold",
        "sb_kinetics": "3. Kinetics & Filters",
        "decay_thresh": "Decay Threshold (ms)",
        "rise_thresh": "Rise Time Threshold (ms)",
        "calc_raw": "Calculate on RAW trace",
        "amp_filter": "Amplitude Filter (>7pA)",
        "col_rise": "Rise Time 10-90% (ms)",
        "col_amp": "Amplitude (pA)",
        "col_iei": "IEI (ms)"
    },
    "Français": {
        "title": "# Pipeline Expert sEPSC : Denoising, Cinétique & Exportation",
        "sb_bessel": "1. Filtre Bessel (Denoising)",
        "cutoff": "Fréquence de coupure (Hz)",
        "nyquist_warn": "⚠️ Limité par la fréquence de Nyquist",
        "sb_detec": "2. Détection Multi-Scale",
        "threshold": "Seuil Z-Score",
        "sb_kinetics": "3. Cinétique & Filtres",
        "decay_thresh": "Seuil Decay (ms)",
        "rise_thresh": "Seuil Rise Time (ms)",
        "calc_raw": "Calculer sur trace BRUTE",
        "amp_filter": "Filtre Amplitude (>7pA)",
        "col_rise": "Rise Time 10-90% (ms)",
        "col_amp": "Amplitude (pA)",
        "col_iei": "IEI (ms)"
    }
}[lang]

# --- FONCTIONS ---
def apply_bessel_filter(data, fs, cutoff=2000, order=4):
    # Sécurité Nyquist : f_cutoff < f_s / 2
    nyquist = 0.5 * fs
    effective_cutoff = min(cutoff, nyquist * 0.95)
    normal_cutoff = effective_cutoff / nyquist
    b, a = signal.bessel(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, data)

def calculate_rise_time_expert(segment_y, dt):
    try:
        peak_idx = np.argmax(segment_y)
        if peak_idx < 3: return 0
        rising_limb = segment_y[:peak_idx + 1]
        t_vec = np.arange(len(rising_limb)) * dt
        peak_val = rising_limb[-1]
        y10, y90 = 0.10 * peak_val, 0.90 * peak_val
        
        # Interpolation pour trouver t10 et t90
        t10 = np.interp(y10, rising_limb, t_vec)
        t90 = np.interp(y90, rising_limb, t_vec)
        return t90 - t10
    except: return 0

# --- SIDEBAR & FILTRES ---
st.sidebar.header(T["sb_bessel"])
use_bessel = st.sidebar.checkbox("Bessel", value=True)
# La limite sera mise à jour dynamiquement après le chargement du fichier
cutoff = st.sidebar.slider(T["cutoff"], 100, int(st.session_state.fs_nyquist), 2000)

st.sidebar.header(T["sb_detec"])
threshold = st.sidebar.slider(T["threshold"], 1.0, 8.0, 2.5)

st.sidebar.header(T["sb_kinetics"])
use_decay_filter = st.sidebar.checkbox("Filter Decay", value=True)
decay_limit = st.sidebar.number_input(T["decay_thresh"], value=3.0, step=0.5)

use_rise_filter = st.sidebar.checkbox("Filter Rise Time", value=True)
rise_limit = st.sidebar.number_input(T["rise_thresh"], value=0.5, step=0.1)

use_amp_filter = st.sidebar.checkbox(T["amp_filter"], value=True)
calc_on_raw = st.sidebar.checkbox(T["calc_raw"], value=False)

# --- LOGIQUE PRINCIPALE ---
file = st.file_uploader("Upload .abf", type=["abf"])

if file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.abf') as tmp:
        tmp.write(file.getvalue())
        tmp_path = tmp.name

    try:
        abf = pyabf.ABF(tmp_path)
        abf.setSweep(0)
        fs, times, dt = abf.dataRate, abf.sweepX, 1000/abf.dataRate
        
        # Mise à jour de la limite de Nyquist dans la session
        nyquist_limit = fs / 2
        st.session_state.fs_nyquist = nyquist_limit
        if cutoff >= nyquist_limit:
            st.sidebar.warning(T["nyquist_warn"])

        raw_data = abf.sweepY - np.median(abf.sweepY)
        f_data = apply_bessel_filter(raw_data, fs, cutoff) if use_bessel else raw_data
        
        # Template Matching Multi-Scale
        best_corr = np.zeros_like(f_data)
        default_decays = [2.0, 5.0, 10.0, 15.0]
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
            # Estimation du decay (τ = Aire / Amplitude)
            estimated_decay = area / amp if amp > 0 else 0
            
            # --- APPLICATION DES NOUVEAUX FILTRES AJUSTABLES ---
            pass_amp = (not use_amp_filter or amp >= 7)
            pass_decay = (not use_decay_filter or estimated_decay <= decay_limit)
            pass_rise = (not use_rise_filter or rise_1090 <= rise_limit)
            
            if pass_amp and pass_decay and pass_rise:
                ev = {'idx': p, 'time': times[p], 'amp': amp, 'rise': rise_1090, 'area': area, 'decay': estimated_decay}
                ev['iei'] = (times[p] - times[peaks[i-1]])*1000 if i>0 else np.nan
                valid_ev.append(ev)

        # Affichage (identique au précédent pour la partie graphique)
        st.markdown(T["title"])
        if valid_ev:
            st.metric("Total Events", len(valid_ev))
            df = pd.DataFrame(valid_ev)
            st.dataframe(df[['time', 'amp', 'rise', 'decay']].head(10))

    except Exception as e: st.error(f"Error: {e}")
    finally:
        if os.path.exists(tmp_path): os.remove(tmp_path)
