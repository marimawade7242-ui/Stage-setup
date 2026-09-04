# Rapport de tests - SenAI Network Lab

## Date des tests

4 septembre 2026

## Environnement de test

- VM1 (LAN) : 192.168.1.10 - Prometheus + Grafana
- VM2 (DMZ) : 192.168.2.10 - node_exporter
- pfSense : 192.168.1.1 (LAN) / 192.168.2.1 (DMZ)

## Tests realises

### Test 1 : Collecte des metriques

Objectif : Verifier que le script collecte correctement les metriques depuis Prometheus.

Commande : python3 network_monitor.py

Resultat : CPU, Memoire, Disque, Reseau - tous OK

Fichiers generes : metrics_export.csv, metrics_export.json

Conclusion : Le script fonctionne correctement.

---

### Test 2 : Detection d'anomalies

Objectif : Verifier que le module detecte les anomalies.

Commande : python3 anomaly_detection.py

Resultat : Modele entraine, anomalies detectees

Fichiers generes : anomaly_results.json, anomaly_results.csv

Conclusion : Le module fonctionne correctement.

---

### Test 3 : Supervision Prometheus

Objectif : Verifier que Prometheus collecte les metriques des 2 nodes.

URL : http://192.168.1.10:9090/targets

Resultat : 2/2 nodes UP

Conclusion : Prometheus supervise correctement.

---

### Test 4 : Dashboard Grafana

Objectif : Verifier que Grafana affiche les metriques.

URL : http://192.168.1.10:3000

Resultat : 4 panels fonctionnels (CPU, Memoire, Disque, Reseau)

Conclusion : Le dashboard fonctionne correctement.

---

### Test 5 : Alertes Prometheus

Objectif : Verifier que les alertes sont configurees.

URL : http://192.168.1.10:9090/alerts

Resultat : 3 alertes configurees (HighCPUUsage, HighMemoryUsage, NodeDown)

Conclusion : Les alertes sont correctement configurees.

---

## Resume des tests

| Test | Statut | Resultat |
|------|--------|----------|
| network_monitor.py | PASS | Collecte fonctionnelle |
| anomaly_detection.py | PASS | Detection fonctionnelle |
| Prometheus targets | PASS | 2/2 nodes UP |
| Grafana dashboard | PASS | 4 panels fonctionnels |
| Prometheus alerts | PASS | 3 alertes configurees |

## Conclusion generale

Tous les tests ont ete valides avec succes.
