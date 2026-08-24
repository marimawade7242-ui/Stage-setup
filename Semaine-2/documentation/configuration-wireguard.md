# Configuration WireGuard sur Ubuntu Desktop

## Installation

WireGuard a été installé avec la commande suivante :

```bash
sudo apt update
sudo apt install wireguard
```

## Fichier de configuration

Le fichier utilisé est :

```text
/etc/wireguard/wg0.conf
```

La configuration réelle n'est pas publiée sur GitHub car elle contient
une clé privée.

Un exemple anonymisé est disponible dans :

```text
configurations/wg0.conf.example
```

## Démarrage du tunnel

```bash
sudo wg-quick up wg0
```

## Arrêt du tunnel

```bash
sudo wg-quick down wg0
```

## Vérification

```bash
sudo wg
```

Cette commande permet de vérifier l'état du tunnel et la date du
dernier handshake.

## Protection du fichier

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
```
