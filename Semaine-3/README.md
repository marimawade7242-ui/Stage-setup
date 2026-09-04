# Semaine 3 – Supervision avec Prometheus et Grafana

##  Objectifs

- Mettre en place une solution de supervision avec Prometheus et Grafana
- Superviser deux machines (LAN et DMZ) derrière un pfSense
- Configurer des alertes (CPU, mémoire, node down)

##  Architecture
Internet
|
pfSense
|--- LAN (192.168.1.0/24)
| |
| +-- VM1 (192.168.1.10)
| - Prometheus
| - Grafana
|
+--- DMZ (192.168.2.0/24)
|
+-- VM2 (192.168.2.10)
- node_exporter (port 9100)

text

##  Contenu du dépôt

| Fichier | Description |
|---------|-------------|
| `prometheus/prometheus.yml` | Configuration de scrape (job `node`) |
| `prometheus/alerts.yml` | Règles d'alerte (CPU, mémoire, node down) |
| `grafana/dashboard.json` | Dashboard CPU / mémoire / disque / réseau |
| `docs/architecture.md` | Schéma et explications de l'architecture |
| `docs/rapport-semaine3.md` | Rapport détaillé de la semaine 3 |

##  Installation rapide

1. Installer Prometheus, node_exporter, Grafana
2. Copier `prometheus.yml` et `alerts.yml` dans `/etc/prometheus/`
3. Redémarrer Prometheus : `sudo systemctl restart prometheus`
4. Importer `grafana/dashboard.json` dans Grafana
5. Vérifier les targets dans Prometheus : `http://192.168.1.10:9090/targets`

##  Règles pfSense

- **LAN → DMZ** :
  - TCP 9100 (node_exporter)
  - ICMP (ping)
