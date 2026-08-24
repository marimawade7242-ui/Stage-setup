# Tests réalisés

## Test 1 : état de WireGuard

Commande :

```bash
sudo wg
```

Résultat attendu :

```text
latest handshake
```

Résultat obtenu :

```text
Handshake établi avec pfSense.
```

Capture associée :

```text
../captures/handshake-wireguard.png
```

## Test 2 : ping vers pfSense

Commande :

```bash
ping -c 4 10.10.10.1
```

Résultat :

```text
Ping réussi.
```

Capture associée :

```text
../captures/ping-pfsense.png
```

## Test 3 : accès au serveur nginx

Commande :

```bash
ping -c 4 192.168.2.10
```

Résultat :

```text
Serveur accessible depuis Ubuntu Desktop.
```

## Test 4 : accès HTTP

Adresse utilisée :

```text
http://192.168.2.10
```

Résultat :

```text
La page Web nginx s'affiche correctement.
```

Capture associée :

```text
../captures/page-nginx.png
```
