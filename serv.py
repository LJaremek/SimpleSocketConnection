import socket

# Setting up host and port
host = "127.0.0.1" # "localhost"
port = 3023

# Making socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Open server
s.bind((host, port))
print("[+] Server on..")

# Open chanel for listening
s.listen()
print("[+] Listening..")

# Waiting for client
conn, addr = s.accept()
print("[+] Client connected")

# Start of waiting for data from client
server_running = True
while server_running:

    # Getting data from client with bufor = 1024
    data = conn.recv(1024)

    # Convert data from bytes to UTF-8
    data = data.decode("UTF-8")

    # Checking if client want to end connection
    if data == "/end":
        server_running = False

    # Printing data if they are not empty
    if data != "":
        print("[>] Client:", data)

print("[-] Client disconnected")
