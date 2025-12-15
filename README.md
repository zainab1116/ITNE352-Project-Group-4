# ITNE352 Project – Group 4

## Project Title
**News Client-Server System using Python**

---

## Project Description
This project is a Python-based client-server system that allows multiple clients to retrieve news information from **NewsAPI.org**.  
The system demonstrates:

- Client-server architecture
- TCP network communication
- Multithreading to handle multiple clients simultaneously
- Fetching and parsing JSON data from an online API
- Organized and readable code structure

The server handles multiple clients and stores news data in JSON files for testing and evaluation. Clients can search for headlines and sources and view details of selected items.

---

## Semester
ITNE352 – Fall 2025

---

## Group
- **Course Code & Section:** ITNE352 – Section 1  
- **Students:**
  - Zainab Jaffar Mohammed Hareem – 202303335
  - Fatema Abbas Abdulla Mohamed – 202305589  

---

## Table of Contents
1. [Requirements](#requirements)  
2. [Setup Instructions](#setup-instructions)  
3. [How to Run](#how-to-run)  
4. [Scripts](#scripts)  
5. [Additional Concepts](#additional-concepts)  
6. [Acknowledgments](#acknowledgments)  
7. [Conclusion](#conclusion)  

---

## Requirements
To run this project locally, you need:

- Python 3.8 or higher
- `requests` library for API calls

Install dependencies using:

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
Ensure you have a folder named data (the server will create it automatically if missing) to store JSON files.

Obtain a valid NewsAPI.org API Key and update the API_KEY variable in server.py.

How to Run
Start the Server
bash
Copy code
python server.py
The server will listen on port 9000 and wait for client connections.

It handles multiple clients simultaneously using threads.

Run the Client
bash
Copy code
python client.py
Enter your name to register with the server.

Navigate menus to search headlines or sources:

Search by keyword, category, country, or list all.

View details of any selected news or source.

Quit to disconnect.

Note: All data retrieved by the server is saved in data/ as JSON files with the format:

text
Copy code
<client_name>_<option>_ITNE352-Group-4.json
Scripts
server.py
Listens for client TCP connections.

Handles multiple clients using threads.

Fetches data from NewsAPI based on client requests.

Saves JSON results in data/ folder.

Displays connection info and request logs on server console.

Main Functions:

fetch_news(endpoint, params) – Fetches API data.

handle_client(conn, addr) – Handles each client in a separate thread.

start_server() – Starts TCP server and waits for connections.

client.py
Connects to the server over TCP.

Displays interactive menus to search for headlines or sources.

Sends requests to server and displays results.

Shows full details of selected items.

Menus:

Main Menu: Search headlines, List of sources, Quit.

Headlines Menu: Search by keywords, category, country, list all.

Sources Menu: Search by category, country, language, list all.

Additional Concepts
Multithreading: The server handles each client in a separate thread, allowing multiple clients to connect simultaneously.

JSON Storage: All retrieved data is saved in JSON files in a dedicated folder for testing and evaluation.

Error Handling: Invalid inputs and API errors are properly handled to prevent server crashes.

Acknowledgments
NewsAPI.org for providing free API access to news data.

Python socket and requests libraries.

University of Bahrain – ITNE352 course resources.

Conclusion
This project demonstrates a fully functional Python client-server system with:

Network communication

API integration

Multithreading

Organized code and proper documentation

Students gained practical experience in building a networked application and handling real-time data from online sources.