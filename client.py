import socket
import json

# ================== CONFIG ==================
SERVER_HOST = '127.0.0.1'  # Server IP
SERVER_PORT = 9000         # Must match server port

# ================== VALID PARAMETERS ==================
VALID_COUNTRIES = ["au", "ca", "jp", "ae", "sa", "kr", "us", "ma"]
VALID_LANGUAGES = ["ar", "en"]
VALID_CATEGORIES = ["business", "general", "health", "science", "sports", "technology"]

# ================== MAIN FUNCTION ==================
def main():
    """Main client function"""
    client_name = input("Enter your name: ")

    # Create socket and connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    client.send(client_name.encode())  # Send client name to server

    # Main loop for menu
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Search headlines")
        print("2. List of sources")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            headlines_menu(client)
        elif choice == '2':
            sources_menu(client)
        elif choice == '3':
            print("Disconnecting...")
            client.close()
            break
        else:
            print("Invalid choice, try again.")

# ================== HEADLINES MENU ==================
def headlines_menu(client):
    """Headlines menu"""
    while True:
        print("\n--- HEADLINES MENU ---")
        print("1. Search by keywords")
        print("2. Search by category")
        print("3. Search by country")
        print("4. List all headlines")
        print("5. Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == '5':
            return  # Back to main menu

        # Get parameter and validate
        param = ''
        if choice == '1':
            param = input("Enter keyword (or press Enter to skip): ").strip()
        elif choice == '2':
            while True:
                param = input(f"Enter category ({', '.join(VALID_CATEGORIES)}): ").strip().lower()
                if param == '' or param in VALID_CATEGORIES:
                    break
                print("Invalid category. Try again.")
        elif choice == '3':
            while True:
                param = input(f"Enter country ({', '.join(VALID_COUNTRIES)}): ").strip().lower()
                if param == '' or param in VALID_COUNTRIES:
                    break
                print("Invalid country. Try again.")

        options_map = {
            '1':'headlines_keywords',
            '2':'headlines_category',
            '3':'headlines_country',
            '4':'headlines_all'
        }
        request = options_map.get(choice) + '|' + param
        client.send(request.encode())  # Send request to server

        # Receive data from server
        data = client.recv(100000).decode()
        data_list = json.loads(data)

        if "info" in data_list:
            print("[INFO] No results found.")
            continue
        elif not isinstance(data_list, list):
            print("[ERROR] Invalid data format from server.")
            continue

        # Display list summary
        for item in data_list:
            print(f"[{item['index']}] {item.get('title', item.get('name'))} | {item.get('source')}")

        # Ask for index to view details
        while True:
            idx_input = input("Select item index to see details: ").strip()
            if not idx_input.isdigit():
                print("Invalid input, try again.")
                continue
            idx = int(idx_input)
            if not (0 <= idx < len(data_list)):
                print("Index out of range, try again.")
                continue
            break

        client.send(str(idx).encode())  # Send selected index to server
        details_data = client.recv(100000).decode()
        details = json.loads(details_data)
        print("\n--- DETAILS ---")
        print(json.dumps(details, indent=4))

# ================== SOURCES MENU ==================
def sources_menu(client):
    """Sources menu"""
    while True:
        print("\n--- SOURCES MENU ---")
        print("1. Search by category")
        print("2. Search by country")
        print("3. Search by language")
        print("4. List all sources")
        print("5. Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == '5':
            return  # Back to main menu

        # Get parameter and validate
        param = ''
        if choice == '1':
            while True:
                param = input(f"Enter category ({', '.join(VALID_CATEGORIES)}): ").strip().lower()
                if param == '' or param in VALID_CATEGORIES:
                    break
                print("Invalid category. Try again.")
        elif choice == '2':
            while True:
                param = input(f"Enter country ({', '.join(VALID_COUNTRIES)}): ").strip().lower()
                if param == '' or param in VALID_COUNTRIES:
                    break
                print("Invalid country. Try again.")
        elif choice == '3':
            while True:
                param = input(f"Enter language ({', '.join(VALID_LANGUAGES)}): ").strip().lower()
                if param == '' or param in VALID_LANGUAGES:
                    break
                print("Invalid language. Try again.")

        options_map = {
            '1':'sources_category',
            '2':'sources_country',
            '3':'sources_language',
            '4':'sources_all'
        }
        request = options_map.get(choice) + '|' + param
        client.send(request.encode())  # Send request to server

        # Receive data from server
        data = client.recv(100000).decode()
        data_list = json.loads(data)

        if "info" in data_list:
            print("[INFO] No results found.")
            continue
        elif not isinstance(data_list, list):
            print("[ERROR] Invalid data format from server.")
            continue

        # Display list summary
        for item in data_list:
            print(f"[{item['index']}] {item.get('name')} |")

        # Ask for index to view details
        while True:
            idx_input = input("Select item index to see details: ").strip()
            if not idx_input.isdigit():
                print("Invalid input, try again.")
                continue
            idx = int(idx_input)
            if not (0 <= idx < len(data_list)):
                print("Index out of range, try again.")
                continue
            break

        client.send(str(idx).encode())  # Send selected index to server
        details_data = client.recv(100000).decode()
        details = json.loads(details_data)
        print("\n--- DETAILS ---")
        print(json.dumps(details, indent=4))

# ================== RUN CLIENT ==================
if __name__ == "__main__":
    main()
