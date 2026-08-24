# Configuration pfSense

## Rôle de pfSense

pfSense assure les fonctions suivantes :

- pare-feu ;
- routage entre les réseaux ;
- serveur WireGuard ;
- contrôle de l'accès à la DMZ.

## Tunnel WireGuard

| Paramètre | Valeur |
|---|---|
| Nom du tunnel | VPN-SenAI |
| Adresse du tunnel | 10.10.10.1/24 |
| Protocole | UDP |
| Port | 51820 |

## Peer configuré

| Paramètre | Valeur |
|---|---|
| Nom | Ubuntu-Desktop |
| Adresse autorisée | 10.10.10.2/32 |
| Clé publique | Non publiée dans ce document |
| Endpoint | Défini côté client |

## Règle pare-feu

Une règle a été créée sur l'interface WireGuard :

```text
Action      : Pass
Protocole   : IPv4
Source      : 10.10.10.0/24
Destination : 192.168.2.0/24
```

Cette règle autorise le client VPN à accéder au serveur Web de la DMZ.

## Sécurité

Les clés privées et les mots de passe ne sont pas affichés.
