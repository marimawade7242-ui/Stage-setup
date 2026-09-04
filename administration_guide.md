# Guide d'administration et de dépannage

## Supervision

### Vérifier l'état des services

```bash
# Prometheus
sudo systemctl status prometheus

# Grafana
sudo systemctl status grafana-server

# node_exporter
sudo systemctl status node_exporter
```

### Redémarrer un service

```bash
sudo systemctl restart prometheus
sudo systemctl restart grafana-server
sudo systemctl restart node_exporter
```

## Diagnostic d'incidents

### 1. Serveur indisponible

**Symptôme** : Target DOWN dans Prometheus

**Diagnostic** :
```bash
ping 192.168.2.10
curl http://192.168.2.10:9100/metrics
```

**Solution** :
```bash
sudo systemctl start node_exporter
```

### 2. Règle firewall incorrecte

**Symptôme** : Timeout entre LAN et DMZ

**Diagnostic** :
```bash
telnet 192.168.2.10 9100
```

**Solution** : Vérifier les règles pfSense LAN → DMZ

### 3. Service arrêté

**Symptôme** : Port non accessible

**Diagnostic** :
```bash
sudo netstat -tlnp | grep 9100
sudo systemctl status node_exporter
```

**Solution** :
```bash
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
```

### 4. Charge anormale

**Symptôme** : CPU/Mémoire > 85%

**Diagnostic** :
```bash
top
htop
free -h
```

**Solution** : Identifier et tuer le processus gourmand

## Automatisation

### Exécuter le script de collecte

```bash
python3 network_monitor.py
```

Fichiers générés :
- `metrics_export.csv`
- `metrics_export.json`

### Exécuter la détection d'anomalies

```bash
python3 anomaly_detection.py
```

Fichiers générés :
- `anomaly_results.json`
- `anomaly_results.csv`

## Commandes utiles

```bash
# Voir les logs Prometheus
sudo journalctl -u prometheus

# Voir les logs Grafana
sudo journalctl -u grafana-server

# Tester la connectivité
ping 192.168.2.10
curl http://192.168.2.10:9100/metrics

# Espace disque
df -h

# Mémoire libre
free -h
```
