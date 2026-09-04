#!/usr/bin/env python3
"""
Network Monitor - Collecte automatique des métriques réseau
SenAI Network Lab - Semaine 4 : Automatisation

Auteur : Ton nom
Date : Septembre 2026
"""

import requests
import json
from datetime import datetime
import csv
import sys

# ============================================================================
# CONFIGURATION
# ============================================================================

PROMETHEUS_URL = "http://localhost:9090"
OUTPUT_CSV = "metrics_export.csv"
OUTPUT_JSON = "metrics_export.json"

# Requêtes Prometheus
QUERIES = {
    "cpu_usage": "100 - (avg by(instance) (rate(node_cpu{mode='idle'}[5m])) * 100)",
    "memory_usage": "(1 - (node_memory_MemAvailable / node_memory_MemTotal)) * 100",
    "disk_usage": "100 - ((node_filesystem_avail / node_filesystem_size) * 100)",
    "network_rx_bytes": "rate(node_network_receive_bytes[5m])",
    "network_tx_bytes": "rate(node_network_transmit_bytes[5m])"
}

# ============================================================================
# FONCTIONS
# ============================================================================

def fetch_metric(query):
    """Récupère une métrique depuis l'API Prometheus"""
    url = f"{PROMETHEUS_URL}/api/v1/query"
    params = {"query": query}
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "success":
            return data["data"]["result"]
        else:
            print(f"Erreur Prometheus : {data.get('error', 'Inconnue')}")
            return []
    
    except requests.exceptions.ConnectionError:
        print(f"Erreur de connexion à Prometheus ({PROMETHEUS_URL})")
        return []
    except Exception as e:
        print(f"Erreur : {e}")
        return []


def collect_all_metrics():
    """Collecte toutes les métriques configurées"""
    metrics = {}
    timestamp = datetime.now().isoformat()
    
    print(f"\nCollecte des métriques à {timestamp}")
    print("-" * 60)
    
    for name, query in QUERIES.items():
        result = fetch_metric(query)
        metrics[name] = result
        status = "OK" if result else "ECHEC"
        print(f"  [{status}] {name}: {len(result)} résultat(s)")
    
    print("-" * 60)
    
    return {
        "timestamp": timestamp,
        "metrics": metrics
    }


def save_to_csv(data, filename=OUTPUT_CSV):
    """Sauvegarde les métriques dans un fichier CSV"""
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Metric", "Instance", "Value"])
            
            for metric_name, results in data["metrics"].items():
                for result in results:
                    instance = result["metric"].get("instance", "unknown")
                    value = result["value"][1]
                    writer.writerow([data["timestamp"], metric_name, instance, value])
        
        print(f"OK - Données CSV sauvegardées dans {filename}")
    
    except Exception as e:
        print(f"Erreur lors de l'écriture CSV : {e}")


def save_to_json(data, filename=OUTPUT_JSON):
    """Sauvegarde les métriques dans un fichier JSON"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"OK - Données JSON sauvegardées dans {filename}")
    
    except Exception as e:
        print(f"Erreur lors de l'écriture JSON : {e}")


def display_summary(data):
    """Affiche un résumé des métriques collectées"""
    print("\n" + "=" * 60)
    print("RÉSUMÉ DE LA COLLECTE")
    print("=" * 60)
    print(f"Timestamp : {data['timestamp']}")
    print(f"Nombre de métriques : {len(data['metrics'])}")
    
    total_points = sum(len(results) for results in data["metrics"].values())
    print(f"Total de points de données : {total_points}")
    
    print("\nDétail par métrique :")
    for metric_name, results in data["metrics"].items():
        if results:
            for result in results:
                instance = result["metric"].get("instance", "unknown")
                value = result["value"][1]
                print(f"  - {metric_name} @ {instance}: {value}")
        else:
            print(f"  - {metric_name}: Aucune donnée")
    
    print("=" * 60)


def main():
    """Fonction principale"""
    print("\n" + "=" * 60)
    print("NETWORK MONITOR - SenAI Network Lab")
    print("Collecte automatique des métriques réseau")
    print("=" * 60)
    
    # Vérification des dépendances
    try:
        import requests
    except ImportError:
        print("\nErreur : Le module 'requests' n'est pas installé")
        print("   Installation : pip3 install requests")
        sys.exit(1)
    
    # 1. Collecte des métriques
    data = collect_all_metrics()
    
    # 2. Sauvegarde
    print("\nSauvegarde des données...")
    save_to_csv(data)
    save_to_json(data)
    
    # 3. Affichage du résumé
    display_summary(data)
    
    # 4. Statut final
    print("\nCOLLECTE TERMINEE AVEC SUCCES !")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
