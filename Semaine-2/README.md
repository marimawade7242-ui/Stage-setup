# Projet réseau — Semaine 2

## Description

La semaine 2 a été consacrée à la mise en place d'un tunnel VPN
WireGuard entre une VM Ubuntu Desktop et le pare-feu pfSense.

L'objectif était de permettre à Ubuntu Desktop d'accéder au serveur Web
nginx situé dans la DMZ à travers le tunnel VPN.

## Architecture réseau

```text
Ubuntu Desktop
Client WireGuard
Adresse VPN : 10.10.10.2
        │
        │ Tunnel WireGuard
        │ UDP 51820
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

## Équipements et adresses IP

| Équipement | Adresse IP | Rôle |
|---|---:|---|
| pfSense | 10.10.10.1 | Pare-feu et serveur WireGuard |
| Ubuntu Desktop | 10.10.10.2 | Client WireGuard |
| Serveur Ubuntu | 192.168.2.10 | Serveur Web nginx dans la DMZ |

## Réseaux utilisés

```text
Réseau VPN WireGuard : 10.10.10.0/24
Réseau DMZ           : 192.168.2.0/24
Port WireGuard       : UDP 51820
```

## Configuration réalisée

Le tunnel WireGuard a été créé sur pfSense avec l'adresse :

```text
10.10.10.1/24
```

Un peer correspondant à Ubuntu Desktop a été ajouté avec l'adresse :

```text
10.10.10.2/32
```

Le serveur nginx est situé dans la DMZ à l'adresse :

```text
192.168.2.10
```

La configuration réelle du client WireGuard n'est pas publiée, car elle
contient une clé privée.

Un fichier de configuration d'exemple est disponible ici :

```text
configurations/wg0.conf.example
```

## Règles pare-feu

Une règle a été créée sur l'interface WireGuard afin d'autoriser
Ubuntu Desktop à accéder au serveur Web de la DMZ.

```text
Action      : Pass
Protocole   : TCP
Source      : 10.10.10.0/24
Destination : 192.168.2.10
Port        : 80
```

Une règle ICMP a également été utilisée pour permettre le test de ping :

```text
Action      : Pass
Protocole   : ICMP
Source      : 10.10.10.0/24
Destination : 192.168.2.10
```

## Tests réalisés

### Vérification du tunnel

```bash
sudo wg
```

Le champ `latest handshake` confirme que le tunnel WireGuard est établi.

### Test de communication avec pfSense

```bash
ping -c 4 10.10.10.1
```

Résultat : test réussi, avec quatre réponses reçues.

### Test d'accès au serveur DMZ

```bash
ping -c 4 192.168.2.10
```

Résultat : le serveur de la DMZ répond correctement.

### Test du serveur Web nginx

```bash
curl http://192.168.2.10
```

L'adresse suivante a également été ouverte dans le navigateur :

```text
http://192.168.2.10
```

Résultat : la page d'accueil nginx s'affiche correctement.

## Captures d'écran

Les captures disponibles sont :

- Handshake WireGuard : `captures/handshake-wireguard.png`
- Ping vers pfSense : `captures/ping-pfsense.png`
- Accès au serveur DMZ : `captures/acces-serveur-dmz.png`
- Règle pare-feu DMZ : `captures/regle-pare-feu-dmz.png`
- Page nginx : `captures/page-nginx.png`

## Difficultés rencontrées

Les principales difficultés rencontrées pendant la configuration
concernaient :

- la distinction entre la clé privée et la clé publique ;
- la différence entre l'adresse du tunnel et l'adresse de l'endpoint ;
- l'absence initiale du handshake WireGuard ;
- la configuration du port UDP `51820` ;
- l'ajout de la règle pare-feu sur l'interface WireGuard ;
- la différence entre un test ping et un test du service Web ;
- la protection des clés privées avant la publication sur GitHub.

Ces problèmes ont été résolus en vérifiant la configuration du tunnel,
les peers, les routes, les règles pare-feu et l'état du service nginx.

## Résultats

Les objectifs de la semaine 2 ont été atteints :

- Le tunnel WireGuard est opérationnel.
- Le handshake entre Ubuntu Desktop et pfSense est établi.
- Ubuntu Desktop peut joindre pfSense.
- Ubuntu Desktop peut accéder au serveur situé dans la DMZ.
- Le serveur nginx répond correctement.
- La page Web est accessible depuis le navigateur.
- Les captures et la documentation ont été ajoutées au dépôt GitHub.

## Documentation

- Compte rendu complet : `compte-rendu/compte-rendu-semaine-2.md`
- Architecture réseau : `documentation/architecture-reseau.md`
- Configuration pfSense : `documentation/configuration-pfsense.md`
- Configuration WireGuard : `documentation/configuration-wireguard.md`
- Tests réalisés : `documentation/tests-realises.md`
- Commandes utilisées : `documentation/commandes-utilisees.md`

## Sécurité

Les informations sensibles ne sont pas publiées dans ce dépôt.

Les éléments suivants ont été exclus :

- les clés privées WireGuard ;
- les mots de passe ;
- les fichiers de configuration réels ;
- les informations publiques sensibles.

Seul le fichier d'exemple suivant est publié :

```text
configurations/wg0.conf.example
```

## Conclusion

La semaine 2 est terminée avec succès.

La mise en place du tunnel WireGuard permet maintenant à Ubuntu Desktop
d'accéder au serveur Web nginx placé dans la DMZ à travers pfSense.
