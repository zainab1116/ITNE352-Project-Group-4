import os
import socket
import threading
import json
import requests

# ================== CONFIG ==================

API_KEY = "c16d6f87b60a4fbfb5b8075d36e74a85"
BASE_URL = "https://newsapi.org/v2/"
GROUP_ID = "ITNE352-Group-4"

HOST = "0.0.0.0"
PORT = 9000

# ================== DATA FOLDER ==================

# Ensure 'data' folder exists
if not os.path.exists("data"):
    os.makedirs("data")

# ================== API FUNCTION ==================

def fetch_news(endpoint, params):
    """
    Fetch data from NewsAPI and return JSON response
    """
    params["apiKey"] = API_KEY
    try:
        response = requests.get(BASE_URL + endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}")
        return {"status": "error"}

# ================== CLIENT HANDLER ==================

def handle_client(conn, addr):
    """
    Handle a single client connection
    """
    try:
        client_name = conn.recv(1024).decode()
        print(f"[NEW CONNECTION] {client_name} connected from {addr}")

        while True:
            request = conn.recv(1024).decode()
            if not request:
                break

            print(f"[REQUEST] {client_name}: {request}")

            # Parse request
            if "|" in request:
                option, param = request.split("|", 1)
            else:
                option, param = request, ""

            option = option.strip()
            param = param.strip()

            # Default parameters
            defaults = {
                "headlines_country": "us",
                "headlines_category": "general",
                "headlines_keywords": "news",
                "sources_country": "us",
                "sources_category": "general",
                "sources_language": "en"
            }

            if not param and option in defaults:
                param = defaults[option]

            # API routing
            if option == "headlines_keywords":
                data = fetch_news("everything", {"q": param})
            elif option == "headlines_category":
                data = fetch_news("top-headlines", {"category": param})
            elif option == "headlines_country":
                data = fetch_news("top-headlines", {"country": param})
            elif option == "headlines_all":
                data = fetch_news("top-headlines", {"country": "us"})
            elif option == "sources_category":
                data = fetch_news("sources", {"category": param})
            elif option == "sources_country":
                data = fetch_news("sources", {"country": param})
            elif option == "sources_language":
                data = fetch_news("sources", {"language": param})
            elif option == "sources_all":
                data = fetch_news("sources", {})
            else:
                conn.send("INVALID".encode())
                continue

            # Save full JSON response
            filename = os.path.join(
                "data", f"{client_name}_{option}_{GROUP_ID}.json"
            )
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            # Prepare summary list
            send_list = []

            if "articles" in data:
                articles = data["articles"][:15]
                for i, a in enumerate(articles):
                    send_list.append({
                        "index": i,
                        "source": a.get("source", {}).get("name"),
                        "author": a.get("author"),
                        "title": a.get("title"),
                        "description": a.get("description")
                    })

            elif "sources" in data:
                sources = data["sources"][:15]
                for i, s in enumerate(sources):
                    send_list.append({
                        "index": i,
                        "id": s.get("id"),
                        "name": s.get("name"),
                        "description": s.get("description"),
                        "url": s.get("url"),
                        "category": s.get("category"),
                        "language": s.get("language"),
                        "country": s.get("country")
                    })

            if not send_list:
                conn.send(json.dumps({"info": "No results"}).encode())
                continue

            # Send list to client
            conn.send(json.dumps(send_list).encode())

            # Receive selected index
            idx_data = conn.recv(1024).decode()
            if not idx_data.isdigit():
                conn.send(json.dumps({"error": "Invalid index"}).encode())
                continue

            idx = int(idx_data)
            if idx < 0 or idx >= len(send_list):
                conn.send(json.dumps({"error": "Index out of range"}).encode())
                continue

            # Send full details
            if "articles" in data:
                conn.send(json.dumps(articles[idx]).encode())
            elif "sources" in data:
                conn.send(json.dumps(sources[idx]).encode())

        print(f"[DISCONNECT] {client_name} disconnected")

    finally:
        conn.close()

# ================== SERVER START ==================

def start_server():
    """
    Start TCP server
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SERVER STARTED] Listening on port {PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
