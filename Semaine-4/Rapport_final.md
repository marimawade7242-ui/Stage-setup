# Rapport Final - Semaine 4

## Automatisation et Détection d'Anomalies

### Objectifs

1. ✅ Automatiser la supervision réseau
2. ✅ Implémenter la détection d'anomalies avec ML
3. ✅ Documenter l'installation et l'administration
4. ✅ Tester et valider les scripts

### Réalisations

#### 1. Network Monitor (`automation/network_monitor.py`)

- Ping automatique des hôtes critiques
- Vérification des ports (SSH, HTTP, HTTPS)
- Statistiques des interfaces réseau
- Exécution manuelle ou planifiée (cron)

#### 2. Anomaly Detection (`anomaly_detection/anomaly_detection.py`)

- Modèle Isolation Forest (scikit-learn)
- Détection de DDoS, scans, pannes
- Classification par sévérité (NORMAL, MEDIUM, HIGH)
- Facile à entraîner avec de nouvelles données

### Technologies

- **Python 3** : Langage principal
- **scikit-learn** : Machine Learning
- **numpy** : Calcul numérique
- **subprocess** : Appels système

### Difficultés Rencontrées

1. Installation de scikit-learn sur Ubuntu
2. Calibration du modèle (contamination)
3. Gestion des timeouts réseau

### Solutions

1. `pip3 install scikit-learn numpy`
2. Tests avec différentes valeurs (0.05 - 0.2)
3. Try/except avec timeout

### Perspectives

- Intégration avec Prometheus/Grafana
- Alertes par email/Slack
- Dashboard de visualisation
- Apprentissage continu (online learning)

### Conclusion

La semaine 4 a permis d'automatiser la supervision et d'ajouter une couche d'intelligence artificielle pour la détection d'anomalies. Le système est opérationnel et prêt pour un déploiement en production.
