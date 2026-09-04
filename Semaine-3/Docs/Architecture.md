# Architecture – Semaine 3

##  Schéma réseau
Internet
|
pfSense
|--- LAN (192.168.1.0/24) - Interface em0
| |
| +-- VM1 (192.168.1.10)
| - Prometheus (port 9090)
| - Grafana (port 3000)
|
+--- DMZ (192.168.2.0/24) - Interface em1
|
+-- VM2 (192.168.2.10)
- node_exporter (port 9100)

text

##  Règles de firewall pfSense

### LAN → DMZ

| Source | Destination | Port | Protocole | Action |
|--------|-------------|------|-----------|--------|
| LAN net | DMZ net | 9100 | TCP | Allow |
| LAN net | DMZ net | - | ICMP | Allow |

### DMZ → LAN

| Source | Destination | Port | Protocole | Action |
|--------|-------------|------|-----------|--------|
| DMZ net | LAN net | - | - | Deny (par défaut) |

##  Flux de supervision

- Prometheus (VM1) scrape :
  - `192.168.1.10:9100` (local)
  - `192.168.2.10:9100` (DMZ)
- Grafana (VM1) affiche les données
- Alertes envoyées vers Alertmanager (optionnel)
