# ITNE352 Project – Group 4

## Project Title
**News Service System – Client/Server Project using Python**

---

## Project Description
A Python-based client-server system that allows multiple clients to retrieve news information from **NewsAPI.org**.  

Features:
- Client-server architecture
- TCP network communication
- Multithreading for multiple simultaneous clients
- Fetching and parsing JSON data from an online API
- Organized and readable code

The server stores news data in JSON files. Clients can search for headlines and sources and view detailed information.

---

## Group
- **Course Code & Section:** ITNE352 – Section 1  
- **Students:**
  - Zainab Jaffar Mohammed Hareem – 202303335
  - Fatema Abbas Abdulla Mohamed – 202305589  

---

## Table of Contents
1. Requirements  
2. Setup Instructions  
3. How to Run  
4. Scripts  
5. Additional Concepts  
6. Acknowledgments  
7. Conclusion  

---

## Requirements
- Python 3.8 or higher  
- `requests` library  

Install dependencies:
```bash
pip install requests
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project folder:

bash
Copy code
cd ITNE352-Project-Group-4
Ensure there is a folder named data (the server will create it automatically if missing).

Obtain a valid NewsAPI.org API Key and update API_KEY in server.py.

How to Run
Start the Server

bash
Copy code
python server.py
Listens on port 9000

Handles multiple clients using threads

Run the Client

bash
Copy code
python client.py
Enter your name to register

Navigate menus to search headlines or sources

View details of selected items

Quit to disconnect

Note: All retrieved data is saved in data/ with the format:
<client_name>_<option>_ITNE352-Group-4.json

Scripts
server.py
Listens for TCP connections

Handles multiple clients with threads

Fetches data from NewsAPI

Saves JSON results in data/

Logs connections and requests

Main functions:

fetch_news(endpoint, params)

handle_client(conn, addr)

start_server()

client.py
Connects to server via TCP

Displays interactive menus

Sends requests and receives results

Shows full details of selected items

Menus:

Main Menu: Search headlines, List of sources, Quit

Headlines Menu: Search by keywords, category, country, list all

Sources Menu: Search by category, country, language, list all

Additional Concepts
Multithreading

JSON storage for testing and evaluation

Error handling for invalid inputs and API failures

Acknowledgments
NewsAPI.org

Python socket and requests libraries

University of Bahrain – ITNE352 course resources

Conclusion
This project demonstrates a fully functional Python client-server system with network communication, API integration, multithreading, organized code, and proper documentation.
Students gained practical experience in building a networked application and handling real-time online data.
