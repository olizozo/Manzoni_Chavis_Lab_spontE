pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Launch the application**:
    ```bash
    streamlitHere is a detailed **README.md** file translated into English for your spontaneous current analysis application (`app_spontE.py`). This document is designed to serve as both a scientific and technical reference for lab students and researchers.

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

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

*Developed for the Chavis Lab | 2026*
*Biophysical Rigor and KineticHere is a detailed **README.md** file translated into English for your spontaneous current analysis application (`app_spontE.py`). This document is designed to serve as both a scientific and technical reference for lab students and researchers.

---

# 🔬 Expert sEPSC Pipeline: Kinetic Analysis & Detection
### *Chavis Lab | Spontaneous Electrophysiology*

This Streamlit application is a dedicated workstation for analyzing spontaneous excitatory post-synaptic currents (**sEPSCs**) or miniature currents (**mEPSCs**). It automates denoising, event detection, and precise kinetic calculations from raw data files (`.abf`).

👉 **Online Access: [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

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

*Developed for the Chavis Lab | 2026*



------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------


Voici un fichier **README.md** extrêmement détaillé pour votre application d'analyse des courants spontanés (`app_spontE.py`). Ce document est conçu pour être utilisé comme référence scientifique et technique pour les étudiants et chercheurs du laboratoire.

---

# 🔬 Pipeline Expert sEPSC : Analyse Cinétique & Détection
### *Chavis Lab | Électrophysiologie Spontanée*

Cette application Streamlit est une station de travail dédiée à l'analyse des courants post-synaptiques excitateurs spontanés (**sEPSC**) ou miniatures (**mEPSC**). Elle automatise le débruitage, la détection d'événements et le calcul précis de la cinétique à partir de fichiers de données brutes (`.abf`).

👉 **Accès en ligne : [https://chavislab-spont.streamlit.app/](https://chavislab-spont.streamlit.app/)**

---

## 📋 Table des Matières
1. [Introduction Scientifique](#1-introduction-scientifique)
2. [Fonctionnalités Clés](#2-fonctionnalités-clés)
3. [Algorithmes et Mathématiques](#3-algorithmes-et-mathématiques)
4. [Guide d'Utilisation](#4-guide-dutilisation)
5. [Limites et Précautions](#5-limites-et-précautions)
6. [Installation Locale](#6-installation-locale)

---

## 1. Introduction Scientifique
L'analyse des courants spontanés est fondamentale pour comprendre les propriétés présynaptiques (probabilité de libération, fréquence) et postsynaptiques (densité de récepteurs, amplitude) d'une synapse. 

L'un des défis majeurs est la détection d'événements de petite taille noyés dans le bruit de fond, tout en mesurant précisément leur temps de montée (Rise Time) et leur charge totale. Ce pipeline répond à ce défi par l'utilisation de filtres à phase linéaire et d'interpolation de données.

---

## 2. Fonctionnalités Clés

* **Filtrage Bessel (Ordre 4)** : Un filtre passe-bas essentiel pour préserver la forme d'onde. Contrairement au filtre Butterworth, le filtre de Bessel ne crée pas d'oscillations artificielles sur les transitions rapides.
* **Détection Multi-Templates** : L'algorithme scanne la trace en utilisant plusieurs modèles de constantes de temps de décroissance (2, 5, 10 et 15 ms) pour s'adapter à la diversité des événements synaptiques.
* **Mesure Cinétique 10-90%** : Calcul précis du temps nécessaire pour passer de 10% à 90% du pic.
* **IEI & Fréquence** : Calcul automatique de l'intervalle inter-événement (IEI) et de la fréquence moyenne en Hertz (Hz).
* **Exportation Double** : 
    * Un fichier "Événements" (chaque ligne = un sEPSC).
    * Un fichier "Population" (statistiques globales et distributions).

---

## 3. Algorithmes et Mathématiques

### Le Filtre de Bessel
Le code applique un filtre de Bessel d'ordre 4. Mathématiquement, ce filtre minimise le délai de groupe, ce qui signifie que toutes les fréquences sont retardées de la même quantité dans la bande passante. Cela garantit que le **Rise Time** mesuré est biologiquement fidèle.

### Interpolation pour la Cinétique
Pour obtenir un Rise Time précis, l'application ne se contente pas des points d'échantillonnage. Elle utilise une **interpolation linéaire** entre les points pour trouver l'instant exact où le signal franchit les seuils de 10% et 90%.



### Calcul de la Charge (Aire)
La charge totale transportée par un événement est calculée par l'intégrale du courant sur la durée de l'événement (jusqu'au retour à la baseline) en utilisant la règle des trapèzes :
$$Charge = \int_{t_{start}}^{t_{end}} I(t) \,dt$$

---

## 4. Guide d'Utilisation

### Étape 1 : Chargement et Paramétrage
1. Chargez votre fichier `.abf`.
2. **Z-Score (Seuil)** : Définissez la sensibilité. Un Z-Score de 4 signifie qu'un événement doit dépasser 4 fois l'écart-type du bruit de fond pour être détecté.
3. **Low-pass Cutoff** : Réglez la fréquence de coupure du filtre (typiquement 1000-2000 Hz).

### Étape 2 : Inspection Visuelle
Utilisez le graphique interactif pour vérifier les détections (marquées en orange).
* **Ajustez le décalage Y** si la baseline de votre cellule n'est pas à 0.
* **Vérifiez les "Doublets"** : Si deux événements sont trop proches, assurez-vous qu'ils sont bien comptés séparément.

### Étape 3 : Statistiques de Population
L'application génère automatiquement trois histogrammes :
* **Distribution d'Amplitude** : Pour voir si une sous-population de grands événements existe.
* **Distribution de Rise Time** : Crucial pour vérifier si les événements sont "bien clampés" (un temps de montée très lent peut indiquer un filtrage dendritique excessif).
* **Distribution IEI** : Pour analyser la régularité de la libération.

---

## 5. Limites et Précautions

1.  **Chevauchement (Doublets)** : Comme tout algorithme automatique, une superposition parfaite de deux EPSCs peut être comptée comme un seul événement large.
2.  **Bruit de Fond** : Si le bruit RMS est trop élevé (> 4-5 pA), la détection des petits minis (< 10 pA) devient statistiquement peu fiable.
3.  **Filtrage excessif** : Un cutoff trop bas (< 500 Hz) lissera artificiellement vos Rise Times et sous-estimera l'amplitude réelle.

---

## 6. Installation Locale

Pour les chercheurs souhaitant modifier le code source :

1.  **Installer Python 3.9+**
2.  **Installer les dépendances** :
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Lancer l'application** :
    ```bash
    streamlit run app_spontE.py
    ```

---

*Développé pour le Chavis Lab | 2026*

