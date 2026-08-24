# Commandes utilisées

## Installation

```bash
sudo apt update
sudo apt install wireguard
```

## Vérification de l'interface

```bash
ip addr show wg0
```

## Démarrage

```bash
sudo wg-quick up wg0
```

## État du tunnel

```bash
sudo wg
```

## Test pfSense

```bash
ping -c 4 10.10.10.1
```

## Test du serveur Web

```bash
ping -c 4 192.168.2.10
curl http://192.168.2.10
```

## Arrêt du tunnel

```bash
sudo wg-quick down wg0
```
