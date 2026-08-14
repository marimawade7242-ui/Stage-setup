# Tests de connectivité – Semaine 1

## Objectif

Vérifier que les machines virtuelles communiquent correctement entre elles et que
le firewall pfSense peut accéder à Internet.

## Machines utilisées

- Firewall : pfSense
- Client LAN : cli-lan (`192.168.1.30`)
- Serveur Web DMZ : srv-web (`192.168.2.10`)

## Résultats

| Source | Destination | Commande | Résultat | Observation |
|---|---|---|---|---|
| pfSense | Internet | `ping 8.8.8.8` | Réussi | Le WAN fonctionne |
| pfSense | Serveur Web | `ping 192.168.2.10` | Réussi | La DMZ fonctionne |
| Client LAN | pfSense LAN | `ping 192.168.1.1` | Réussi | Le LAN fonctionne |
| Serveur Web | Internet | `ping 8.8.8.8` | À corriger | NAT/règles firewall à configurer en semaine 2 |

## Conclusion

Les réseaux LAN et DMZ ont été créés et validés.
Le firewall pfSense accède à Internet avec le NAT VirtualBox.
La sortie Internet du serveur Web de la DMZ sera configurée pendant la semaine 2.
