import socket

def scan_ports(target, port_range):
    """Scanne les ports d'un hôte donné dans une plage spécifiée."""
    print(f"Scanning ports on {target}...")

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 seconde pour chaque connexion
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()

def main():
    print("=== Port Scanner ===")
    target = input("Enter the target IP or domain (e.g., example.com): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    # Créer une plage de ports à scanner
    port_range = range(start_port, end_port + 1)

    # Scanner les ports
    scan_ports(target, port_range)

if __name__ == "__main__":
    main()
