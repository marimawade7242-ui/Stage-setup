# Rapport – Semaine 3 : Supervision

##  Objectifs

1. Mettre en place Prometheus et Grafana
2. Superviser deux machines (LAN et DMZ)
3. Configurer des alertes (CPU, mémoire, node down)
4. Configurer les règles pfSense pour autoriser les flux

## ✅ Travaux réalisés

### 1. Installation des composants

- **VM1 (192.168.1.10)** :
  - Prometheus
  - Grafana
- **VM2 (192.168.2.10)** :
  - node_exporter

### 2. Configuration pfSense

- Création de la règle LAN → DMZ :
  - TCP 9100 (node_exporter)
  - ICMP (ping)

### 3. Configuration Prometheus

- Ajout du job `node` dans `prometheus.yml`
- Définition des règles d'alerte dans `alerts.yml`

### 4. Création du dashboard Grafana

- Panels :
  - CPU usage par instance
  - Mémoire usage par instance
  - Disque usage par instance
  - Réseau (tx/rx) par instance

### 5. Tests

- Vérification des targets : `http://192.168.1.10:9090/targets`
- Vérification des alertes : `http://192.168.1.10:9090/alerts`
- Tests de charge CPU : `yes > /dev/null &`

##  Difficultés rencontrées

- **Problème** : node_exporter inaccessible depuis VM1
- **Solution** : Ajout de la règle pfSense LAN → DMZ (TCP 9100)

- **Problème** : Alertes ne se déclenchent pas
- **Solution** : Correction des expressions (utilisation de `node_cpu` au lieu de `node_cpu_seconds_total`)

##  Résultats

- ✅ Les deux targets sont UP dans Prometheus
- ✅ Le dashboard Grafana affiche les métriques
- ✅ Les alertes se déclenchent correctement

##  Conclusion

La supervision est opérationnelle pour les deux machines. Les alertes permettent de détecter :
- Une surcharge CPU (> 80% pendant 5 min)
- Une surcharge mémoire (> 85% pendant 5 min)
- Une panne de node_exporter (> 1 min)
