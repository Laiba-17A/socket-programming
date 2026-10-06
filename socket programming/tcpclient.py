
import socket

# Create a TCP socket
# AF_INET = IPv4
# SOCK_STREAM = TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port
HOST = '127.0.0.1'
PORT = 5000

# Connect to the server
client_socket.connect((HOST, PORT))

print("Connected to the server.")

# Message that we want to send
message = "Hello from Client!"

# Convert string to bytes and send it to the server
client_socket.send(message.encode())

# Receive response from server
data = client_socket.recv(1024).decode()

print("Message from server:", data)

# Close the connection
client_socket.close()

print("Client closed.")