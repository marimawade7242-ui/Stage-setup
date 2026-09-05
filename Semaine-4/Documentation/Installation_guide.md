# Guide d'Installation - Semaine 4

## Automatisation et Détection d'Anomalies

### Prérequis

- Python 3.8+
- scikit-learn
- numpy

### Installation

```bash
# Installer les dépendances
pip3 install scikit-learn numpy

# Vérifier l'installation
python3 --version
pip3 list | grep -E "scikit|numpy"
```

### Structure des fichiers
semaine4/
├── automation/
│ └── network_monitor.py
├── anomaly_detection/
│ └── anomaly_detection.py
└── documentation/
├── installation_guide.md
├── administration_guide.md
└── test_report.md

text

### Tests

```bash
# Tester le script de monitoring
python3 automation/network_monitor.py

# Tester la détection d'anomalies
python3 anomaly_detection/anomaly_detection.py
```

### Résolution des problèmes

**Erreur : ModuleNotFoundError**
```bash
pip3 install scikit-learn numpy
```

**Erreur : Permission denied**
```bash
chmod +x automation/network_monitor.py
chmod +x anomaly_detection/anomaly_detection.py
```
