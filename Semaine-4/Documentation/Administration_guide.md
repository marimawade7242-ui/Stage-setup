
# Guide d'Administration - Semaine 4

## Supervision Automatisée

### Lancer le monitoring

```bash
cd semaine4
python3 automation/network_monitor.py
```

### Planifier avec cron

```bash
# Éditer crontab
crontab -e

# Ajouter une tâche toutes les 5 minutes
*/5 * * * * /usr/bin/python3 /home/mariama/semaine4/automation/network_monitor.py >> /var/log/network_monitor.log 2>&1
```

## Détection d'Anomalies

### Lancer la détection

```bash
cd semaine4
python3 anomaly_detection/anomaly_detection.py
```

### Interpréter les résultats

- **Anomaly: False** = Trafic normal
- **Anomaly: True, Severity: MEDIUM** = Anomalie modérée
- **Anomaly: True, Severity: HIGH** = Anomalie critique

### Personnaliser le modèle

Modifier `contamination` dans `IsolationForest` :
- `0.05` = Plus strict (moins de faux positifs)
- `0.2` = Plus permissif (détecte plus d'anomalies)

## Logs et Surveillance

```bash
# Voir les logs
tail -f /var/log/network_monitor.log

# Statistiques
grep -c "Anomaly: True" /var/log/network_monitor.log
```
