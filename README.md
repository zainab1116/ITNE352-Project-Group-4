ITNE352 Project – Group 4
News Service System – Client/Server Project using Python
A Python-based client-server system that allows multiple clients to retrieve news information from NewsAPI.org. The system includes client-server architecture, TCP network communication, multithreading for multiple clients, fetching and parsing JSON data from an online API, and organized, readable code. The server stores news data in JSON files. Clients can search for headlines and sources and view detailed information.

Team Members
Name Student ID
Zainab Jaffar Mohammed Hareem 202303335
Fatema Abbas Abdulla Mohamed 202305589

🧩 Task Distribution
Task Number Description Assigned Student
Task 1 Server Setup, TCP Connections, Multithreading Zainab
Task 2 Client Menus, Requests, Data Display Fatema
Task 3 API Integration, JSON Storage Zainab & Fatema
Task 4 Error Handling, Validation, Testing Zainab & Fatema

📦 Project Summary
This project includes:

Server script (server.py) that listens for TCP connections, handles multiple clients using threads, fetches data from NewsAPI, saves JSON results in a data/ folder, and logs connections and requests.

Client script (client.py) that connects to the server via TCP, displays interactive menus, sends requests, receives results, and shows full details of selected items.

Menus: Main Menu (Search headlines, List of sources, Quit), Headlines Menu (Search by keywords, category, country, list all), Sources Menu (Search by category, country, language, list all).

Multithreading to handle multiple simultaneous clients.

JSON storage for testing and evaluation.

Proper error handling for invalid inputs and API failures.

🛠 Technologies Used
Programming: Python 3.8+
Libraries: requests for API calls, socket for networking, threading for multithreading
API: NewsAPI.org
Data Format: JSON

🚀 How to Run

Clone the repository: git clone <repository-url>

Navigate to the project folder: cd ITNE352-Project-Group-4

Ensure a folder named data exists (the server will create it automatically if missing).

Update the API_KEY variable in server.py with a valid NewsAPI.org API key.

Start the server: python server.py (listens on port 9000, handles multiple clients with threads).

Run the client: python client.py (enter your name to register, navigate menus, view details, quit to disconnect).

All retrieved data is saved in data/ as <client_name>_<option>_ITNE352-Group-4.json.

Acknowledgments
NewsAPI.org for providing API access to news data.
Python socket and requests libraries.
University of Bahrain – ITNE352 course resources.

Conclusion
This project demonstrates a fully functional Python client-server system with network communication, API integration, multithreading, organized code, and proper documentation. Students gained practical experience in building a networked application and handling real-time online data.
