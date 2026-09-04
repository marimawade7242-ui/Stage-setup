# Rapport Final - Projet Reseau SenAI

## Resume

Ce document presente le projet de supervision reseau mis en place dans le cadre du stage SenAI Technologies.

## 1. Introduction

### Contexte

Mise en place d'une infrastructure reseau supervisee avec :
- Segmentation reseau (LAN, DMZ)
- Supervision des performances
- Detection d'anomalies
- Automatisation des taches

### Objectifs

- Superviser 2 machines virtuelles
- Collecter les metriques CPU, memoire, disque, reseau
- Configurer des alertes de supervision
- Automatiser la collecte des metriques
- Detecter les comportements anormaux

## 2. Architecture reseau

### Schema

Internet
   |
 pfSense
   |--- LAN (192.168.1.0/24)
   |       |
   |       +-- VM1 (192.168.1.10)
   |              - Prometheus
   |              - Grafana
   |
   +--- DMZ (192.168.2.0/24)
           |
           +-- VM2 (192.168.2.10)
                  - node_exporter

### Plan d'adressage

| Reseau | CIDR | Interface |
|--------|------|-----------|
| LAN | 192.168.1.0/24 | pfSense em0 |
| DMZ | 192.168.2.0/24 | pfSense em1 |

### Matrice des flux

| Source | Destination | Port | Protocole | Action |
|--------|-------------|------|-----------|--------|
| LAN | DMZ | 9100 | TCP | Allow |
| LAN | DMZ | - | ICMP | Allow |
| DMZ | LAN | - | - | Deny |

## 3. Supervision

### Prometheus

- Collecte des metriques toutes les 15 secondes
- 2 cibles configurees (VM1 et VM2)
- 3 alertes configurees :
  - HighCPUUsage (>80% pendant 5min)
  - HighMemoryUsage (>85% pendant 5min)
  - NodeDown (node_exporter down pendant 1min)

### Grafana

- Dashboard avec 4 panels :
  - CPU Usage
  - Memory Usage
  - Disk Usage
  - Network Traffic
- Rafraichissement automatique : 30 secondes

## 4. Automatisation

### Script network_monitor.py

- Collecte automatique des metriques depuis Prometheus
- Export en CSV et JSON
- Requetes : CPU, Memoire, Disque, Reseau RX/TX

### Script anomaly_detection.py

- Utilisation de Isolation Forest (scikit-learn)
- Entraine sur des donnees normales
- Detection des anomalies (CPU/memoire eleves)
- Export des resultats en JSON et CSV

## 5. Tests et validation

### Tests realises

| Test | Resultat |
|------|----------|
| Collecte metriques | PASS |
| Detection anomalies | PASS |
| Prometheus targets | PASS (2/2 UP) |
| Grafana dashboard | PASS (4 panels) |
| Alertes Prometheus | PASS (3 alertes) |

### Incidents testes

- Serveur indisponible : Detecte par NodeDown
- Charge CPU anormale : Detectee par HighCPUUsage
- Memoire elevee : Detectee par HighMemoryUsage

## 6. Difficultes rencontrees

### Probleme 1 : Noms de metriques

Probleme : Les metriques node_exporter utilisaient des noms differents.

Solution : Adaptation des requetes PromQL.

### Probleme 2 : Firewall pfSense

Probleme : node_exporter inaccessible depuis le LAN.

Solution : Ajout de la regle firewall LAN -> DMZ (TCP 9100).

### Probleme 3 : Espace disque

Probleme : Disque plein (98%) lors de l'installation.

Solution : Installation via apt au lieu de pip3.

## 7. Conclusion

### Bilan

L'infrastructure de supervision est operationnelle avec :
- 2 machines supervisees
- 5 metriques collectees
- 3 alertes configurees
- 2 scripts d'automatisation
- Detection d'anomalies fonctionnelle

### Competences acquises

- TCP/IP, sous-reseaux, routage
- Segmentation reseau et filtrage (pfSense)
- Administration Linux
- Supervision (Prometheus, Grafana)
- Python applique au reseau
- Detection d'anomalies (Machine Learning)
- Documentation technique

### Perspectives

- Ajouter Alertmanager pour les notifications
- Ameliorer la detection d'anomalies
- Ajouter d'autres metriques
- Mettre en place des rapports automatiques
