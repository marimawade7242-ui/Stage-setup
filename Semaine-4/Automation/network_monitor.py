#!/usr/bin/env python3
"""
Network Monitoring Automation Script
Semaine 4 - Automatisation de la supervision réseau
"""

import subprocess
import json
from datetime import datetime

def ping_host(host):
    """Ping a host and return latency"""
    try:
        result = subprocess.run(
            ['ping', '-c', '1', host],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            # Extract latency from ping output
            for line in result.stdout.split('\n'):
                if 'time=' in line:
                    latency = line.split('time=')[1].split(' ')[0]
                    return {'status': 'up', 'latency': latency}
        return {'status': 'down', 'latency': None}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

def check_port(host, port):
    """Check if a port is open"""
    try:
        result = subprocess.run(
            ['nc', '-z', '-w', '2', host, str(port)],
            capture_output=True
        )
        return result.returncode == 0
    except:
        return False

def get_network_stats():
    """Get network interface statistics"""
    try:
        result = subprocess.run(
            ['cat', '/proc/net/dev'],
            capture_output=True,
            text=True
        )
        return result.stdout
    except:
        return None

def main():
    """Main monitoring function"""
    print(f"=== Network Monitor - {datetime.now()} ===\n")
    
    # Hosts to monitor
    hosts = ['192.168.1.1', '192.168.2.1', '192.168.2.10']
    
    for host in hosts:
        result = ping_host(host)
        print(f"Host: {host}")
        print(f"  Status: {result['status']}")
        if result['status'] == 'up':
            print(f"  Latency: {result['latency']}")
        
        # Check common ports
        for port in [22, 80, 443]:
            if check_port(host, port):
                print(f"  Port {port}: OPEN")
        
        print()
    
    # Network stats
    print("=== Network Interface Stats ===")
    stats = get_network_stats()
    if stats:
        print(stats)

if __name__ == '__main__':
    main()
