# 🔬 Pipeline Expert sEPSC : Denoising, Cinétique & Exportation

Cette application Streamlit est une station de travail avancée pour l'analyse des courants post-synaptiques excitateurs spontanés (**sEPSC**). Elle permet de passer de fichiers bruts (`.abf`) à une analyse cinétique complète et exportable en quelques minutes.

👉 **[Accéder à l'application en ligne](https://chavislab-spont.streamlit.app/)**

---

## 🌟 Points Forts du Pipeline

* **Denoising Intelligent** : Utilisation d'un filtre de Bessel d'ordre 4 pour éliminer le bruit tout en préservant l'intégrité de la cinétique des événements (Rise Time).
* **Détection Multi-Scale** : Algorithme de détection basé sur des templates à constantes de temps de décroissance multiples (2, 5, 10, 15 ms) pour capturer les événements de toutes tailles.
* **Analyse Cinétique Experte** : Calcul précis de l'amplitude, du Rise Time (10-90% avec interpolation), de la charge (aire) et de l'IEI (Intervalle Inter-Événement).
* **Filtres de Qualité** : Options pour exclure les événements de faible amplitude (< 7 pA) ou à décroissance anormale.

---

## 🛠️ Fonctionnalités Détaillées

### 1. Prétraitement (Denoising)
* **Filtre de Bessel** : Contrairement aux filtres standards, le filtre de Bessel offre une phase linéaire, évitant les oscillations artificielles lors de la détection de pics rapides.
* **Cutoff ajustable** : Réglage précis de la fréquence de coupure (500 Hz à 5000 Hz).

### 2. Détection & Analyse
* **Z-Score dynamique** : Seuil de détection ajustable basé sur l'écart-type du bruit de fond.
* **Calcul sur trace brute ou filtrée** : Liberté de calculer la cinétique finale sur les données originales pour plus de précision.
* **Rise Time 10-90%** : Recherche inversée et interpolation pour une mesure précise du temps de montée.

### 3. Visualisation & Exportation
* **Zoom Interactif** : Contrôle total sur les axes X et Y pour inspecter chaque détection.
* **Exportation CSV** : Génération de rapports complets incluant les statistiques par événement et les distributions de population.

---

## 🚀 Guide Rapide

1.  **Chargement** : Glissez votre fichier `.abf` dans la zone de téléchargement.
2.  **Configuration** : Réglez le seuil de détection (Z-Score) dans la barre latérale.
3.  **Inspection** : Vérifiez visuellement les détections (marquées en orange) sur la trace.
4.  **Export** : Téléchargez le fichier CSV pour vos analyses statistiques ou vos graphiques sous Prism/R.

---

## 💻 Installation Locale

Si vous souhaitez exécuter ce pipeline sur votre machine :

1.  **Prérequis** : Assurez-vous d'avoir Python 3.9+ installé.
2.  **Installation des bibliothèques** :
    ```bash
    pip install streamlit pyabf numpy matplotlib scipy pandas
    ```
3.  **Lancement** :
    ```bash
    streamlit run app_spontE.py
    ```

---

## 📑 Crédits & Labo
Développé pour la communauté des neurosciences et le **Chavis Lab**. 
*Cet outil utilise `pyabf` pour l'accès natif aux fichiers Axon Binary Format.*

---

### Aperçu Mathématique
L'application intègre des méthodes d'intégration trapézoïdale pour le calcul de la charge et des algorithmes de recherche de seuils précis pour la cinétique de montée.


---

*Contact : Pour toute question ou demande de fonctionnalité, contactez olivier.manzoni@inserm.fr.*
