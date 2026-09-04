#!/usr/bin/env python3
"""
Détection d'anomalies - Isolation Forest
SenAI Network Lab - Semaine 4 : Automatisation & ML

Auteur : Ton nom
Date : Septembre 2026
"""

import numpy as np
from sklearn.ensemble import IsolationForest
import json
from datetime import datetime
import csv

# ============================================================================
# CLASSE : Détecteur d'anomalies
# ============================================================================

class AnomalyDetector:
    """Détecteur d'anomalies basé sur Isolation Forest"""
    
    def __init__(self, contamination=0.1):
        """
        Initialise le détecteur
        
        Args:
            contamination: Proportion estimée d'anomalies (0.0 à 0.5)
        """
        self.model = IsolationForest(
            contamination=contamination,
            random_state=42,
            n_estimators=100
        )
        self.is_fitted = False
        self.training_data = []
    
    def train(self, data):
        """
        Entraîne le modèle avec des données normales
        
        Args:
            data: Liste de listes [[cpu, mem, disk], ...]
        """
        print(f"Entraînement avec {len(data)} échantillons...")
        X = np.array(data)
        self.model.fit(X)
        self.is_fitted = True
        self.training_data = data
        print("Modèle entraîné avec succès ✓")
    
    def predict(self, data_point):
        """
        Prédit si un point est une anomalie
        
        Args:
            data_point: [cpu, mem, disk]
        
        Returns:
            Dictionnaire avec status, prediction, score, data
            -1 = Anomalie, 1 = Normal
        """
        if not self.is_fitted:
            raise Exception("Modèle non entraîné !")
        
        X = np.array([data_point])
        prediction = self.model.predict(X)[0]
        score = self.model.score_samples(X)[0]
        
        status = "ANOMALIE" if prediction == -1 else "NORMAL"
        return {
            "status": status,
            "prediction": int(prediction),
            "score": float(score),
            "data": data_point
        }
    
    def analyze_batch(self, data_points):
        """
        Analyse plusieurs points de données
        
        Args:
            data_points: Liste de points [[cpu, mem, disk], ...]
        
        Returns:
            Dictionnaire avec results et summary
        """
        results = []
        for point in data_points:
            result = self.predict(point)
            results.append(result)
        
        # Statistiques
        anomalies = sum(1 for r in results if r["status"] == "ANOMALIE")
        normal = len(results) - anomalies
        
        return {
            "results": results,
            "summary": {
                "total": len(results),
                "anomalies": anomalies,
                "normal": normal,
                "anomaly_rate": anomalies / len(results) * 100
            }
        }

# ============================================================================
# GÉNÉRATION DE DONNÉES
# ============================================================================

def create_training_data():
    """
    Crée un jeu de données d'entraînement (comportement normal)
    
    Returns:
        Liste de 100 échantillons [cpu, mem, disk]
    """
    np.random.seed(42)
    
    normal_data = []
    for _ in range(100):
        cpu = np.random.uniform(20, 60)      # 20-60%
        mem = np.random.uniform(30, 70)      # 30-70%
        disk = np.random.uniform(40, 60)     # 40-60%
        normal_data.append([cpu, mem, disk])
    
    return normal_data


def create_test_data():
    """
    Crée des données de test (normales + anormales)
    
    Returns:
        Liste de 20 échantillons [cpu, mem, disk]
    """
    test_data = []
    
    # Données normales (10)
    for _ in range(10):
        cpu = np.random.uniform(20, 60)
        mem = np.random.uniform(30, 70)
        disk = np.random.uniform(40, 60)
        test_data.append([cpu, mem, disk])
    
    # Anomalies - CPU très élevé (5)
    for _ in range(5):
        cpu = np.random.uniform(85, 95)      # > 85%
        mem = np.random.uniform(30, 70)
        disk = np.random.uniform(40, 60)
        test_data.append([cpu, mem, disk])
    
    # Anomalies - Mémoire très élevée (5)
    for _ in range(5):
        cpu = np.random.uniform(20, 60)
        mem = np.random.uniform(90, 98)      # > 90%
        disk = np.random.uniform(40, 60)
        test_data.append([cpu, mem, disk])
    
    return test_data

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def save_results(results, filename="anomaly_results.json"):
    """Sauvegarde les résultats dans un fichier JSON"""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nRésultats sauvegardés dans {filename}")


def save_results_csv(results, filename="anomaly_results.csv"):
    """Sauvegarde les résultats dans un fichier CSV"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Point", "Status", "CPU", "Memory", "Disk", "Score"])
        
        for i, result in enumerate(results["results"]):
            writer.writerow([
                i + 1,
                result["status"],
                f"{result['data'][0]:.2f}",
                f"{result['data'][1]:.2f}",
                f"{result['data'][2]:.2f}",
                f"{result['score']:.4f}"
            ])
    
    print(f"Résultats CSV sauvegardés dans {filename}")

# ============================================================================
# FONCTION PRINCIPALE
# ============================================================================

def main():
    """Fonction principale de démonstration"""
    print("\n" + "=" * 60)
    print("DÉTECTION D'ANOMALIES - Isolation Forest")
    print("SenAI Network Lab - Semaine 4")
    print("=" * 60)
    
    # 1. Création des données
    print("\n[1] Création des données d'entraînement...")
    train_data = create_training_data()
    print(f"    {len(train_data)} échantillons normaux créés")
    
    print("\n[2] Création des données de test...")
    test_data = create_test_data()
    print(f"    {len(test_data)} échantillons de test créés")
    print("    (10 normaux + 5 CPU élevé + 5 Mémoire élevée)")
    
    # 2. Entraînement
    print("\n[3] Entraînement du modèle...")
    detector = AnomalyDetector(contamination=0.1)
    detector.train(train_data)
    
    # 3. Analyse
    print("\n[4] Analyse des données de test...")
    results = detector.analyze_batch(test_data)
    
    # 4. Affichage des résultats
    print("\n" + "=" * 60)
    print("RÉSULTATS")
    print("=" * 60)
    
    summary = results["summary"]
    print(f"\nTotal analysé : {summary['total']} points")
    print(f"Normaux : {summary['normal']}")
    print(f"Anomalies : {summary['anomalies']}")
    print(f"Taux d'anomalies : {summary['anomaly_rate']:.1f}%")
    
    print("\n" + "-" * 60)
    print("ANOMALIES DÉTECTÉES")
    print("-" * 60)
    
    anomalies_found = False
    for i, result in enumerate(results["results"]):
        if result["status"] == "ANOMALIE":
            anomalies_found = True
            print(f"\n  Point {i+1}: {result['status']}")
            print(f"    CPU: {result['data'][0]:.1f}%")
            print(f"    Mémoire: {result['data'][1]:.1f}%")
            print(f"    Disque: {result['data'][2]:.1f}%")
            print(f"    Score: {result['score']:.4f}")
    
    if not anomalies_found:
        print("\n  Aucune anomalie détectée")
    
    print("\n" + "=" * 60)
    print("DÉMONSTRATION TERMINÉE")
    print("=" * 60)
    
    # 5. Sauvegarde
    save_results(results)
    save_results_csv(results)

if __name__ == "__main__":
    main()
