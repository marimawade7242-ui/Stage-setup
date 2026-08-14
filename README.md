# Stage Setup

Projet de stage – Réseaux et Infrastructure.

## Objectif

Concevoir et mettre en œuvre un laboratoire virtuel de réseau d’entreprise
sécurisé avec segmentation LAN/DMZ, supervision automatisée et détection
d’anomalies.

## Technologies utilisées

- VirtualBox
- pfSense
- Ubuntu Server
- Prometheus
- Grafana
- Python
- scikit-learn
- Git et GitHub

## Architecture réseau actuelle

- WAN : NAT VirtualBox
- Firewall : pfSense
- LAN : 192.168.1.0/24
  - pfSense LAN : 192.168.1.1
  - Client LAN : 192.168.1.30
- DMZ : 192.168.2.0/24
  - pfSense DMZ : 192.168.2.1
  - Serveur Web : 192.168.2.10

## Avancement

- [x] Semaine 1 : architecture et laboratoire virtuel
- [ ] Semaine 2 : sécurisation, règles firewall et VPN
- [ ] Semaine 3 : supervision et alertes
- [ ] Semaine 4 : automatisation et détection d’anomalies# Stage-setup
