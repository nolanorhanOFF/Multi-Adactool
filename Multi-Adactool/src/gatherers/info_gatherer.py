import socket
import requests

def get_ip_info(domain):
    """Récupère l'adresse IP d'un domaine."""
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP address of {domain}: {ip_address}")
        return ip_address
    except socket.gaierror:
        print(f"Could not resolve {domain}")
        return None

def get_whois_info(domain):
    """Récupère des informations WHOIS pour un domaine."""
    try:
        response = requests.get(f"https://api.whois.vu/?q={domain}")
        if response.status_code == 200:
            whois_info = response.json()
            print(f"WHOIS information for {domain}:")
            print(whois_info)
        else:
            print(f"Could not retrieve WHOIS information for {domain}")
    except Exception as e:
        print(f"An error occurred while retrieving WHOIS info: {e}")

def gather_info(domain):
    """Effectue la collecte d'informations sur un domaine donné."""
    print(f"Gathering information for {domain}...\n")
    
    # Récupérer l'adresse IP
    ip_info = get_ip_info(domain)
    
    # Récupérer les informations WHOIS
    if ip_info:
        get_whois_info(domain)

def main():
    print("=== Info Gatherer ===")
    domain = input("Enter the domain to gather information (e.g., example.com): ")
    
    # Effectuer la collecte d'informations
    gather_info(domain)

if __name__ == "__main__":
    main()
