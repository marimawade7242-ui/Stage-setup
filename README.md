# Stage Setup

Projet de stage – Réseaux et Infrastructure.

## Objectif

Concevoir et mettre en œuvre un laboratoire virtuel de réseau d'entreprise sécurisé avec segmentation LAN/DMZ, supervision automatisée et détection d'anomalies.

## Technologies utilisées

- VirtualBox
- pfSense
- Ubuntu Server
- **Prometheus** (supervision)
- **Grafana** (dashboarding)
- Python
- scikit-learn
- Git et GitHub

## Architecture réseau actuelle

- **WAN** : NAT VirtualBox
- **Firewall** : pfSense
- **LAN** : 192.168.1.0/24
  - pfSense LAN : 192.168.1.1
  - Client LAN : 192.168.1.30
  - **Serveur Monitoring** : 192.168.1.10
    - Prometheus : port 9090
    - Grafana : port 3000
- **DMZ** : 192.168.2.0/24
  - pfSense DMZ : 192.168.2.1
  - Serveur Web : 192.168.2.10

## Structure du dépôt
Stage-setup/
├── architecture/
│ ├── network_diagram/ # Diagramme réseau
│ └── ip_addressing_plan/ # Plan d'adressage IP
├── firewall/
│ └── rules_documentation/ # Règles firewall + matrice des flux
├── vpn/
│ └── configuration/ # Config WireGuard/OpenVPN
├── monitoring/
│ ├── prometheus/ # Config Prometheus (prometheus.yml)
│ │ └── prometheus.yml
│ └── grafana/ # Dashboard Grafana
│ ├── dashboard.json
│ └── captures/
├── automation/
│ └── network_monitor.py # Script Python de monitoring
├── anomaly_detection/
│ └── anomaly_detection.py # Script Python de détection d'anomalies
├── tests/
│ └── test_report/ # Rapport de tests
└── documentation/
├── installation_guide.md # Guide d'installation
├── administration_guide.md # Guide d'administration
└── rapport_final.md # Rapport final

text

## Avancement

- [x] Semaine 1 : architecture et laboratoire virtuel
- [x] Semaine 2 : sécurisation, règles firewall et VPN
- [x] Semaine 3 : supervision et alertes (Prometheus + Grafana)
- [x] Semaine 4 : automatisation et détection d'anomalies
- [ ] Documentation finale et rapport

## Livrables

### Semaine 1 - Architecture
- [x] Diagramme d'architecture
- [x] Plan d'adressage IP
- [x] Laboratoire virtuel fonctionnel

### Semaine 2 - Sécurité
- [x] Matrice des flux
- [x] Configuration firewall documentée
- [x] VPN fonctionnel

### Semaine 3 - Supervision
- [x] Dashboard de supervision (Grafana)
- [x] Règles d'alerte configurées
- [x] Scénarios de panne testés

### Semaine 4 - Automatisation
- [x] Scripts Python d'automatisation
- [x] Module de détection d'anomalies
- [x] Documentation technique

### Finalisation
- [ ] Rapport final de stage
- [ ] Présentation de soutenance

## Dashboard de supervision

Le dashboard Grafana inclut :
- **CPU/RAM** des serveurs
- **Disponibilité** des services (ping)
- **Latence** réseau
- **Pertes de paquets**
- **Services monitorés** : SSH, HTTP, HTTPS
