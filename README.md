
# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. https://doi.org/10.5281/zenodo.19915015**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    Voici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | ÉlectrophysiVoici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.Voici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (202Voici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19Voici](https://doi.org/10.5281/zenodo.19Voici) le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptVoici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptiques (probabilité de libération, fréquence) et postsynaptiques (densité de récepteurs, amplitude) d'une synapse. 

LVoici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptiques (probabilité de libération, fréquence) et postsynaptiques (densité de récepteurs, amplitude) d'une synapse. 

L'un des défis majeurs est la détection d'événements de petite taille noyés dans le bruit de fond, tout en mesurant précisément leur temps de montée (RiseVoici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptiques (probabilité de libération, fréquence) et postsynaptiques (densité de récepteurs, amplitude) d'une synapse. 

L'un des défis majeurs est la détection d'événements de petite taille noyés dans le bruit de fond, tout en mesurant précisément leur temps de montée (Rise Time) et leur charge totale. Ce pipeline répond à ce défi par l'utilisation de filtres à phase linéaire et d'interpolation de données.

---

*Voici le fichier **README.md** bilingue mis à jour. J'ai ajouté une section **Citation** incluant le badge DOI officiel et la référence académique pour permettre aux chercheurs de citer correctement votre travail[cite: 1].

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
If you use this software in your research, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)]([https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015))

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 📋 Table of Contents
1. [Scientific Introduction](#1-scientific-introduction)
2. [Key Features](#2-key-features)
3. [Algorithms and Mathematics](#3-algorithms-and-mathematics)
4. [User Guide](#4-user-guide)
5. [Limitations and Precautions](#5-limitations-and-precautions)
6. [Local Installation](#6-local-installation)

---

## 1. Scientific Introduction
The analysis of spontaneous currents is fundamental to understanding the presynaptic properties (release probability, frequency) and postsynaptic properties (receptor density, amplitude) of a synapse.

One of the major challenges is detecting small events buried in background noise while precisely measuring their Rise Time and total charge. This pipeline addresses this challenge through the use of linear phase filters and data interpolation.



---

## 2. Key Features
*   **Bessel Filtering (4th Order)**: A low-pass filter essential for preserving waveform integrity. Unlike the Butterworth filter, the Bessel filter does not create artificial oscillations (ringing) on fast transitions.
*   **Multi-Template Detection**: The algorithm scans the trace using several decay time constant templates (2, 5, 10, and 15 ms) to adapt to the diversity of synaptic events.
*   **10-90% Kinetic Measurement**: Precise calculation of the time required to rise from 10% to 90% of the peak.
*   **IEI & Frequency**: Automatic calculation of the Inter-Event Interval (IEI) and mean frequency in Hertz (Hz).
*   **Double Export**: 
    *   An "Events" file (each row = one sEPSC).
    *   A "Population" file (global statistics and distributions).

---

## 3. Algorithms and Mathematics

### The Bessel Filter
The code applies a 4th-order Bessel filter. Mathematically, this filter minimizes group delay, meaning all frequencies are delayed by the same amount within the bandwidth. This ensures that the measured **Rise Time** remains biologically faithful.

### Interpolation for Kinetics
To obtain a precise Rise Time, the application does not rely solely on sampling points. It uses **linear interpolation** between points to find the exact moment the signal crosses the 10% and 90% thresholds.

### Charge Calculation (Area)
The total charge carried by an event is calculated by integrating the current over the duration of the event (until the return to baseline) using the trapezoidal rule:
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. User Guide

### Step 1: Loading and Setup
1. Upload your `.abf` file.
2. **Z-Score (Threshold)**: Define the sensitivity. A Z-Score of 4 means an event must exceed 4 times the standard deviation of the background noise to be detected.
3. **Low-pass Cutoff**: Set the filter cutoff frequency (typically 1000-2000 Hz).

### Step 2: Visual Inspection
Use the interactive graph to verify detections (marked in orange).
*   **Adjust the Y-offset** if your cell's baseline is not at 0.
*   **Check for "Doublets"**: If two events are too close, ensure they are counted separately.

### Step 3: Population Statistics
The app automatically generates three histograms:
*   **Amplitude Distribution**: To see if a sub-population of large events exists.
*   **Rise Time Distribution**: Crucial for checking if events are "well-clamped" (a very slow rise time can indicate excessive dendritic filtering).
*   **IEI Distribution**: To analyze the regularity of release.

---

## 5. Limitations and Precautions
1.  **Overlapping (Doublets)**: Like any automatic algorithm, a perfect superposition of two EPSCs may be counted as a single large event.
2.  **Background Noise**: If the RMS noise is too high (> 4-5 pA), detecting small minis (< 10 pA) becomes statistically unreliable.
3.  **Excessive Filtering**: A cutoff that is too low (< 500 Hz) will artificially smooth your Rise Times and underestimate the true amplitude.

---

## 6. Local Installation
For researchers wishing to modify the source code:

1.  **Install Python 3.9+**
2.  **Install dependencies**:
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlit run app_spontE.py
    ```

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection (FR)
### *Chavis Lab | Électrophysiologie Spontanée*

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 🎓 Citation
Si vous utilisez ce logiciel dans vos recherches, merci de le citer comme suit :

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19915015.svg)](https://doi.org/10.5281/zenodo.19915015)

> **Manzoni, O. J. (2026). Manzoni_Chavis_Lab_spontE. Zenodo. [https://doi.org/10.5281/zenodo.19915015](https://doi.org/10.5281/zenodo.19915015)**

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptiques (probabilité de libération, fréquence) et postsynaptiques (densité de récepteurs, amplitude) d'une synapse. 

L'un des défis majeurs est la détection d'événements de petite taille noyés dans le bruit de fond, tout en mesurant précisément leur temps de montée (Rise Time) et leur charge totale. Ce pipeline répond à ce défi par l'utilisation de filtres à phase linéaire et d'interpolation de données.

---

*Developed for the Chavis Lab | 2026*
*Biophysical Rigor and Kinetic Precision.*
