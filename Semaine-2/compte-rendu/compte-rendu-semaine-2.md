# Compte rendu — Semaine 2

## 1. Objectif

L'objectif de la semaine 2 était de mettre en place un tunnel VPN
WireGuard entre une VM Ubuntu Desktop et le pare-feu pfSense.

Ce tunnel devait permettre à Ubuntu Desktop d'accéder au serveur Web
nginx installé dans la DMZ.

## 2. Architecture réseau

L'architecture utilisée est la suivante :

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

## 3. Équipements utilisés

| Équipement | Adresse | Rôle |
|---|---|---|
| pfSense | 10.10.10.1 | Pare-feu et serveur WireGuard |
| Ubuntu Desktop | 10.10.10.2 | Client WireGuard |
| Serveur Ubuntu | 192.168.2.10 | Serveur Web nginx dans la DMZ |

Le réseau VPN utilisé est :

```text
10.10.10.0/24
```

Le réseau DMZ utilisé est :

```text
192.168.2.0/24
```

## 4. Configuration de WireGuard

Un tunnel WireGuard a été créé sur pfSense avec les paramètres suivants :

```text
Nom du tunnel : VPN-SenAI
Adresse VPN   : 10.10.10.1/24
Protocole     : UDP
Port          : 51820
```

Un peer correspondant à Ubuntu Desktop a ensuite été ajouté :

```text
Nom               : Ubuntu-Desktop
Adresse autorisée : 10.10.10.2/32
```

Sur Ubuntu Desktop, le fichier de configuration utilisé est :

```text
/etc/wireguard/wg0.conf
```

La configuration contient notamment :

```ini
[Interface]
Address = 10.10.10.2/24

[Peer]
AllowedIPs = 10.10.10.0/24, 192.168.2.0/24
PersistentKeepalive = 25
```

Les clés privées ne sont pas publiées dans le dépôt GitHub pour des
raisons de sécurité.

## 5. Règle pare-feu

Une règle a été créée sur l'interface WireGuard de pfSense afin
d'autoriser le client VPN à accéder au serveur Web de la DMZ.

```text
Action      : Pass
Protocole   : TCP
Source      : 10.10.10.0/24
Destination : 192.168.2.10
Port        : 80
Description : Autoriser HTTP Ubuntu VPN vers nginx DMZ
```

Une règle ICMP a également été utilisée pour permettre le test de ping :

```text
Action      : Pass
Protocole   : ICMP
Source      : 10.10.10.0/24
Destination : 192.168.2.10
Description : Autoriser ping Ubuntu VPN vers serveur DMZ
```

Après la création des règles, les modifications ont été sauvegardées
avec le bouton `Apply Changes`.

## 6. Tests réalisés

### 6.1 Vérification du tunnel WireGuard

La commande suivante a été utilisée sur Ubuntu Desktop :

```bash
sudo wg
```

La présence de la mention `latest handshake` a confirmé que le tunnel
était établi entre Ubuntu Desktop et pfSense.

Capture associée :

```text
captures/handshake-wireguard.png
```

### 6.2 Test vers pfSense

La commande suivante a été exécutée :

```bash
ping -c 4 10.10.10.1
```

Le ping a réussi avec quatre réponses reçues et aucune perte de paquet.

Ce test confirme la communication entre Ubuntu Desktop et pfSense à
travers le tunnel WireGuard.

Capture associée :

```text
captures/ping-pfsense.png
```

### 6.3 Test d'accès au serveur DMZ

La commande suivante a été exécutée :

```bash
ping -c 4 192.168.2.10
```

Le serveur situé dans la DMZ a répondu correctement.

Ce test confirme qu'Ubuntu Desktop peut atteindre le réseau DMZ à
travers le VPN et les règles pare-feu de pfSense.

Capture associée :

```text
captures/acces-serveur-dmz.png
```

### 6.4 Test du service Web nginx

L'adresse suivante a été ouverte dans le navigateur :

```text
http://192.168.2.10
```

La page d'accueil nginx s'est affichée correctement.

Un test supplémentaire a également été réalisé avec la commande :

```bash
curl http://192.168.2.10
```

Ces tests confirment que le service Web nginx est accessible depuis
Ubuntu Desktop.

Capture associée :

```text
captures/page-nginx.png
```

## 7. Difficultés rencontrées

### 7.1 Confusion entre les clés

Une première difficulté concernait la distinction entre la clé privée
et la clé publique.

La clé privée doit rester sur la machine qui l'a générée. La clé
publique doit être communiquée à l'autre équipement. Une vérification
des clés a donc été nécessaire sur pfSense et Ubuntu Desktop.

### 7.2 Configuration de l'adresse VPN

Une confusion a également eu lieu entre l'adresse du tunnel WireGuard
et l'adresse IP habituelle de pfSense.

L'adresse utilisée pour tester pfSense à travers le VPN est :

```text
10.10.10.1
```

L'adresse du client Ubuntu Desktop est :

```text
10.10.10.2
```

Le test correct est donc :

```bash
ping -c 4 10.10.10.1
```

### 7.3 Configuration de l'endpoint

L'endpoint correspond à l'adresse permettant au client de joindre
pfSense, avec le port WireGuard :

```text
ADRESSE_PFSENSE:51820
```

Il ne fallait pas confondre l'endpoint avec l'adresse VPN `10.10.10.1`.

### 7.4 Absence initiale du handshake

Au début, la commande `sudo wg` n'affichait pas de handshake récent.

Les éléments suivants ont été vérifiés :

- les clés publiques et privées ;
- l'adresse de l'endpoint ;
- le port UDP `51820` ;
- l'état du tunnel ;
- la configuration du peer ;
- les règles pare-feu.

Après correction de la configuration, le handshake a été établi.

### 7.5 Règle pare-feu manquante

Le ping vers le serveur DMZ ne fonctionnait pas avant l'ajout de la
règle pare-feu sur l'interface WireGuard.

La règle a été configurée pour autoriser le réseau VPN :

```text
10.10.10.0/24
```

vers le serveur Web de la DMZ :

```text
192.168.2.10
```

Une règle ICMP a aussi été ajoutée pour permettre le test de ping.

### 7.6 Différence entre ping et accès Web

Le ping permet uniquement de vérifier la connectivité réseau. Il ne
prouve pas que le service Web fonctionne.

Pour vérifier nginx, il a donc fallu utiliser :

```bash
curl http://192.168.2.10
```

et ouvrir l'adresse suivante dans le navigateur :

```text
http://192.168.2.10
```

### 7.7 Protection des informations sensibles

La configuration réelle de WireGuard contient une clé privée. Elle ne
doit pas être déposée sur GitHub.

Seul un fichier d'exemple anonymisé a été ajouté :

```text
configurations/wg0.conf.example
```

Les clés privées, les mots de passe et les informations sensibles ont
été retirés des captures et des fichiers publiés.

## 8. Résultats obtenus

Les tests suivants ont été validés :

- Tunnel WireGuard établi.
- Handshake visible avec la commande `sudo wg`.
- Ping vers pfSense réussi avec l'adresse `10.10.10.1`.
- Ping vers le serveur DMZ réussi avec l'adresse `192.168.2.10`.
- Accès HTTP au serveur nginx réussi.
- Page nginx affichée dans le navigateur.
- Règles pare-feu configurées sur pfSense.

## 9. Conclusion

La mise en place du VPN WireGuard entre Ubuntu Desktop et pfSense est
terminée avec succès.

Ubuntu Desktop peut maintenant accéder à pfSense et au serveur Web nginx
situé dans la DMZ. Les difficultés rencontrées concernant les clés, les
adresses IP, l'endpoint, le handshake et les règles pare-feu ont été
résolues.

La configuration et les preuves de fonctionnement ont été ajoutées
dans le dépôt GitHub. La semaine 2 est donc terminée et le projet peut
passer à la semaine 3.
