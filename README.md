# Reverse-Shell
🔐 Note: This is for educational purposes only. Do not deploy without permission.
🧠 Explanation:
Code Part	Purpose
socket.socket()	Creates a TCP socket
subprocess.check_output()	Runs commands and captures output
recv() and send()	Send and receive commands/responses
while True	Persistent loop for session

# 🕳️ Python Reverse Shell (Client-Server)

> ⚠️ For ethical hacking labs, learning and red-team practice only.

This is a basic reverse shell written in Python. It allows remote command-line access between two machines over a TCP socket.

---

## 📦 Features

- TCP socket-based remote shell
- Executes OS commands and returns output
- Lightweight and easy to modify
- Works on Windows/Linux

---

## 🔧 Requirements

- Python 3.x

---

## ⚙️ Usage

### 🖥️ Server (Attacker)

python reverse_shell_server.py

🧑‍💻 Client (Victim/Test)

Edit reverse_shell_client.py:

server_ip = 'YOUR_SERVER_IP'

Then run:

python reverse_shell_client.py


📌 Commands

Use standard terminal commands (e.g., ls, cd, whoami, ipconfig, pwd).

🔒 Disclaimer

This project is meant for educational use only in controlled environments. Never use this on unauthorized systems.
