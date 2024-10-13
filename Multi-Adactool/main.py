import os

def display_menu():
    print("=== Multi Adactool ===")
    print("1. Port Scanner")
    print("2. Network Scanner")
    print("3. Vulnerability Scanner")
    print("4. SQL Injector")
    print("5. Info Gatherer")
    print("6. DoS Attack")
    print("7. Phishing Tool")
    print("8. Quit")

def print_banner():
    banner = """
▄▄▄      ▓█████▄  ▄▄▄       ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒████▄    ▒██▀ ██▌▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒██  ▀█▄  ░██   █▌▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░██▄▄▄▄██ ░▓█▄   ▌░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
 ▓█   ▓██▒░▒████▓  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
 ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ▒   ▒▒ ░ ░ ▒  ▒   ▒   ▒▒ ░  ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░   ▒    ░ ░  ░   ░   ▒   ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░  ░   ░          ░  ░░ ░                   ░ ░      ░ ░      ░  ░
           ░                ░                                           
    """
    print(banner)

def main():
    print_banner()  # Affiche le texte ASCII art
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            os.system('python src/scanners/port_scanner.py')
        elif choice == '2':
            os.system('python src/scanners/network_scanner.py')
        elif choice == '3':
            os.system('python src/analyzers/vulnerability_scanner.py')
        elif choice == '4':
            os.system('python src/analyzers/sql_injector.py')
        elif choice == '5':
            os.system('python src/gatherers/info_gatherer.py')
        elif choice == '6':
            os.system('python src/attacks/dos_attack.py')
        elif choice == '7':
            os.system('python src/attacks/phishing_tool.py')
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
