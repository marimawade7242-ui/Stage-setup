# Architecture réseau

## Schéma

```text
Ubuntu Desktop
10.10.10.2
     │
     │ Tunnel WireGuard
     │ UDP 51820
     │
pfSense
10.10.10.1
     │
     │ Règle pare-feu
     │
DMZ
192.168.2.0/24
     │
Serveur nginx
192.168.2.10
```

## Description

Ubuntu Desktop établit un tunnel WireGuard vers pfSense.
Le trafic destiné au réseau VPN et à la DMZ passe par ce tunnel.

pfSense contrôle ensuite l'accès grâce à ses règles pare-feu.
Le serveur nginx reste placé dans la DMZ.
