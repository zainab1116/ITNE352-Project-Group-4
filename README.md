ITNE352 Project – Group 4
News Service System – Client/Server Project using Python

A Python-based client-server system that allows multiple clients to retrieve news information from NewsAPI.org. The system includes:

Client-server architecture

TCP network communication

Multithreading for multiple simultaneous clients

Fetching and parsing JSON data from an online API

Organized and readable code

The server stores news data in JSON files. Clients can search for headlines and sources and view detailed information.

Team Members
| Name                          | Student ID |
| ----------------------------- | ---------- |
| Zainab Jaffar Mohammed Hareem | 202303335  |
| Fatema Abbas Abdulla Mohamed  | 202305589  |

🧩 Task Distribution
| Task Number | Description                                   | Assigned Student |
| ----------- | --------------------------------------------- | ---------------- |
| Task 1      | Server Setup, TCP Connections, Multithreading | Zainab           |
| Task 2      | Client Menus, Requests, Data Display          | Fatema           |
| Task 3      | API Integration, JSON Storage                 | Zainab & Fatema  |
| Task 4      | Error Handling, Validation, Testing           | Zainab & Fatema  |

📦 Project Summary

This project includes:

Server script (server.py)

Listens for TCP connections

Handles multiple clients using threads

Fetches data from NewsAPI

Saves JSON results in data/ folder

Logs connections and requests

Client script (client.py)

Connects to server via TCP

Displays interactive menus

Sends requests and receives results

Shows full details of selected items

Menus:

Main Menu: Search headlines, List of sources, Quit

Headlines Menu: Search by keywords, category, country, list all

Sources Menu: Search by category, country, language, list all

Features:

Multithreading to handle multiple simultaneous clients

JSON storage for testing and evaluation

Proper error handling for invalid inputs and API failures

🛠 Technologies Used

Programming: Python 3.8+

Libraries: requests, socket, threading

API: NewsAPI.org

Data Format: JSON

🚀 How to Run

Clone the repository:

git clone <repository-url>


Navigate to the project folder:

cd ITNE352-Project-Group-4


Ensure a folder named data exists (server will create it automatically if missing).

Update the API_KEY variable in server.py with a valid NewsAPI.org API key.

Start the Server:

python server.py


Listens on port 9000

Handles multiple clients using threads

Run the Client:

python client.py


Enter your name to register

Navigate menus to search headlines or sources

View details of selected items

Quit to disconnect

All retrieved data is saved in data/ as:

<client_name>_<option>_ITNE352-Group-4.json

Acknowledgments

NewsAPI.org for providing API access to news data

Python socket and requests libraries

University of Bahrain – ITNE352 course resources

Conclusion

This project demonstrates a fully functional Python client-server system with:

- Network communication

- API integration

- Multithreading

- Organized code and proper documentation

Through this project, we gained hands-on experience in developing a networked application and managing real-time data from online sources, which enhanced our practical skills in software development.
