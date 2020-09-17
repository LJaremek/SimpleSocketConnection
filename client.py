import socket

# Setting up host and port
host = "127.0.0.1" # "localhost"
port = 3023

# Making socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying of connection to the server
try:
    
    # Connecting to the server
    s.connect((host, port))
    print("[+] Connection successful")
    client_running = True
    
except ConnectionError:
    
    print("[-] Connection failed")
    client_running = False

# Start of waiting for data and sending it
while client_running:

    # Input the data
    text = input("Text to send: ")

    # Checking if client want to end connection
    if text == "/end":
        client_running = False

    # Encode text from UTF-8 to bytes
    text = text.encode("UTF-8")

    # Send text in bytes to server
    s.sendall(text)

print("[-] Disconnected")
