# Projet réseau — Semaine 2

## Description

Durant la semaine 2, un tunnel VPN WireGuard a été configuré entre
une VM Ubuntu Desktop et le pare-feu pfSense.

L'objectif est de permettre à Ubuntu Desktop d'accéder au serveur Web
nginx situé dans la DMZ.

## Architecture réseau

```text
Ubuntu Desktop
Client WireGuard
Adresse VPN : 10.10.10.2
        │
        │ Tunnel WireGuard
        │
pfSense
Serveur WireGuard
Adresse VPN : 10.10.10.1
        │
        │ Règles pare-feu
        │
DMZ
        │
Serveur nginx
Adresse IP : 192.168.2.10
```

## Adressage IP

| Équipement | Adresse IP | Fonction |
|---|---:|---|
| pfSense | 10.10.10.1 | Serveur WireGuard |
| Ubuntu Desktop | 10.10.10.2 | Client WireGuard |
| Serveur nginx | 192.168.2.10 | Serveur Web dans la DMZ |

## Résultats

- Tunnel WireGuard opérationnel.
- Handshake établi.
- Ping vers pfSense réussi.
- Accès à la DMZ réussi.
- Page Web nginx accessible depuis Ubuntu Desktop.

## Documentation

- [Compte rendu](compte-rendu/compte-rendu-semaine-2.md)
- [Configuration pfSense](documentation/configuration-pfsense.md)
- [Configuration WireGuard](documentation/configuration-wireguard.md)
- [Tests réalisés](documentation/tests-realises.md)
- [Architecture réseau](documentation/architecture-reseau.md)

## Sécurité

Les clés privées, mots de passe et informations publiques sensibles
ne sont pas publiés dans ce dépôt.
