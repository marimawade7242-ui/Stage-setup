# Compte rendu — Semaine 2

## 1. Objectif

L'objectif de cette semaine était de mettre en place un accès VPN
avec WireGuard entre Ubuntu Desktop et pfSense.

Cet accès devait permettre à Ubuntu Desktop d'atteindre le serveur
nginx installé dans la DMZ.

## 2. Architecture

L'architecture comprend :

- pfSense comme pare-feu et serveur VPN ;
- Ubuntu Desktop comme client WireGuard ;
- Ubuntu Server comme serveur Web nginx ;
- un réseau VPN WireGuard en 10.10.10.0/24 ;
- un réseau DMZ en 192.168.2.0/24.

## 3. Configuration réalisée

Le tunnel WireGuard a été créé sur pfSense avec l'adresse :

10.10.10.1/24

Le peer Ubuntu Desktop utilise l'adresse :

10.10.10.2/32

Le serveur Web nginx est accessible à l'adresse :

192.168.2.10

## 4. Règles pare-feu

Une règle a été ajoutée sur l'interface WireGuard afin d'autoriser
le trafic provenant du réseau VPN vers la DMZ.

Source : 10.10.10.0/24  
Destination : 192.168.2.0/24  
Action : Pass

## 5. Tests

Les tests suivants ont été réalisés :

- vérification du handshake WireGuard ;
- ping vers 10.10.10.1 ;
- accès à 192.168.2.10 ;
- ouverture de la page nginx dans un navigateur.

## 6. Difficultés

Les principales difficultés concernaient :

- la distinction entre clé privée et clé publique ;
- la configuration de l'endpoint ;
- la différence entre le port d'écoute et le port local ;
- l'ajout de la règle pare-feu WireGuard.

## 7. Conclusion

Le tunnel WireGuard est fonctionnel. Ubuntu Desktop peut accéder
à pfSense ainsi qu'au serveur nginx placé dans la DMZ.

La semaine 2 est donc terminée avec succès.
