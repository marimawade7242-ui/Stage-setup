# Plan d’adressage IP

## Réseau WAN

| Équipement | Interface | Adresse IP | Masque | Rôle |
|---|---|---|---|---|
| pfSense | WAN | 10.0.2.15 | /24 | Accès Internet via NAT VirtualBox |

> L’adresse WAN est attribuée automatiquement par DHCP via le NAT de VirtualBox.

## Réseau LAN

Réseau : `192.168.1.0/24`

| Équipement | Interface | Adresse IP | Passerelle | Rôle |
|---|---|---|---|---|
| pfSense | LAN | 192.168.1.1/24 | — | Passerelle du réseau LAN |
| Client Ubuntu | enp0s3 | 192.168.1.30/24 | 192.168.1.1 | Machine de test LAN |

## Réseau DMZ

Réseau : `192.168.2.0/24`

| Équipement | Interface | Adresse IP | Passerelle | Rôle |
|---|---|---|---|---|
| pfSense | DMZ | 192.168.2.1/24 | — | Passerelle du réseau DMZ |
| Serveur Web Ubuntu | enp0s3 | 192.168.2.10/24 | 192.168.2.1 | Serveur Web de démonstration |

## Réseaux VirtualBox

| Nom du réseau | Type VirtualBox | Utilisation |
|---|---|---|
| WAN | NAT | Connexion de pfSense vers Internet |
| intnet_lan | Réseau interne | Communication entre pfSense et le client LAN |
| intnet_dmz | Réseau interne | Communication entre pfSense et le serveur Web |
