# Compte rendu – Semaine 1

## Objectif

Mettre en place le laboratoire virtuel réseau avec un firewall pfSense,
un réseau LAN, un réseau DMZ et les premières machines Ubuntu.

## Travaux réalisés

- Installation et utilisation de VirtualBox.
- Création de la VM firewall pfSense.
- Création du réseau WAN en NAT VirtualBox.
- Création du réseau interne LAN : `intnet_lan`.
- Création du réseau interne DMZ : `intnet_dmz`.
- Configuration des interfaces pfSense :
  - WAN : 10.0.2.15 (DHCP VirtualBox)
  - LAN : 192.168.1.1/24
  - DMZ : 192.168.2.1/24
- Création du serveur Web Ubuntu dans la DMZ :
  - IP : 192.168.2.10/24
  - Passerelle : 192.168.2.1
- Création du client Ubuntu dans le LAN :
  - IP : 192.168.1.30/24
  - Passerelle : 192.168.1.1

## Tests réalisés

- Ping pfSense vers Internet (`8.8.8.8`) : réussi.
- Ping pfSense vers le serveur Web (`192.168.2.10`) : réussi.
- Ping du client LAN vers pfSense (`192.168.1.1`) : réussi.

## Difficultés rencontrées

- Configuration des adresses IP statiques avec Netplan.
- Paramétrage des réseaux internes dans VirtualBox.
- La sortie Internet depuis la DMZ doit encore être configurée avec les règles
  firewall et le NAT lors de la semaine 2.

## Prochaines étapes

- Configurer les règles firewall entre LAN, DMZ et Internet.
- Mettre en place le NAT pour la DMZ.
- Installer un serveur Web de démonstration dans la DMZ.
- Préparer la matrice de flux réseau.
- Configurer un VPN de test.
