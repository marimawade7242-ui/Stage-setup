# Guide d'installation - SenAI Network Lab

## Prérequis

- 3 machines virtuelles (pfSense, VM1, VM2)
- 8 Go RAM minimum
- 50 Go disque

## Étape 1 : Installation de pfSense

1. Télécharger pfSense depuis https://www.pfsense.org
2. Créer la VM avec 2 interfaces réseau
3. Configurer les interfaces :
   - WAN : DHCP (NAT)
   - LAN : 192.168.1.1/24
   - DMZ : 192.168.2.1/24

## Étape 2 : Configuration des VMs

### VM1 (LAN - 192.168.1.10)

```bash
# Installation Prometheus
sudo apt update
sudo apt install prometheus prometheus-node-exporter -y

# Installation Grafana
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install grafana -y
sudo systemctl start grafana-server
```

### VM2 (DMZ - 192.168.2.10)

```bash
# Installation node_exporter
sudo apt install prometheus-node-exporter -y
sudo systemctl start node_exporter
```

## Étape 3 : Configuration pfSense

1. Aller dans Firewall → Rules → LAN
2. Ajouter une règle :
   - Action: Allow
   - Destination: DMZ net
   - Port: 9100 (TCP)
3. Ajouter une règle ICMP pour le ping

## Étape 4 : Vérification

- Prometheus: http://192.168.1.10:9090/targets
- Grafana: http://192.168.1.10:3000

## Étape 5 : Scripts Python

### Installer les dépendances

```bash
sudo apt install python3-sklearn python3-numpy python3-scipy python3-requests -y
```

### Tester les scripts

```bash
python3 network_monitor.py
python3 anomaly_detection.py
```
