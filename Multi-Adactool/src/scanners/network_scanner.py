import scapy.all as scapy

def scan_network(ip_range):
    """Scanne le réseau pour découvrir les hôtes actifs."""
    print(f"Scanning network: {ip_range}...")
    
    # Envoie une requête ARP pour découvrir les hôtes
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("Active hosts:")
    for element in answered_list:
        print(f"IP: {element[1].psrc} | MAC: {element[1].hwsrc}")

def main():
    print("=== Network Scanner ===")
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.1/24): ")
    
    # Scanner le réseau
    scan_network(ip_range)

if __name__ == "__main__":
    main()
