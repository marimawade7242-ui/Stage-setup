#!/usr/bin/env python3
"""
Anomaly Detection Script
Semaine 4 - Détection d'anomalies réseau avec scikit-learn
"""

import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime
import json

# Sample network traffic data (packets per second, bytes per second, connections)
# Format: [packets/s, bytes/s, active_connections]
normal_traffic = [
    [100, 50000, 10],
    [120, 55000, 12],
    [95, 48000, 9],
    [110, 52000, 11],
    [105, 51000, 10],
    [115, 53000, 11],
    [98, 49000, 10],
    [108, 50500, 10],
    [102, 51500, 11],
    [112, 52500, 12],
]

# Anomalous traffic patterns
anomalous_traffic = [
    [500, 250000, 50],   # DDoS attack
    [10, 5000, 2],       # Network outage
    [1000, 500000, 100], # Massive scan
]

def train_model(data):
    """Train isolation forest model"""
    X = np.array(data)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    return model

def detect_anomaly(model, sample):
    """Detect if a sample is anomalous"""
    prediction = model.predict([sample])[0]
    score = model.score_samples([sample])[0]
    
    if prediction == -1:
        return {'anomaly': True, 'score': score, 'severity': 'HIGH' if score < -0.5 else 'MEDIUM'}
    else:
        return {'anomaly': False, 'score': score, 'severity': 'NORMAL'}

def main():
    """Main anomaly detection function"""
    print(f"=== Anomaly Detection - {datetime.now()} ===\n")
    
    # Train model on normal traffic
    print("Training model on normal traffic...")
    model = train_model(normal_traffic)
    print("Model trained successfully!\n")
    
    # Test on normal traffic
    print("=== Testing Normal Traffic ===")
    for i, sample in enumerate(normal_traffic[:3]):
        result = detect_anomaly(model, sample)
        print(f"Sample {i+1}: {sample}")
        print(f"  Anomaly: {result['anomaly']} | Severity: {result['severity']}")
        print()
    
    # Test on anomalous traffic
    print("=== Testing Anomalous Traffic ===")
    for i, sample in enumerate(anomalous_traffic):
        result = detect_anomaly(model, sample)
        print(f"Sample {i+1}: {sample}")
        print(f"  Anomaly: {result['anomaly']} | Severity: {result['severity']}")
        print()
    
    # Summary
    print("=== Summary ===")
    print("Normal traffic samples: 10")
    print("Anomalous traffic samples: 3")
    print("Model: Isolation Forest (contamination=0.1)")
    print("\nDetection complete!")

if __name__ == '__main__':
    main()
