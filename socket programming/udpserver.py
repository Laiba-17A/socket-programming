import socket

# Create a UDP socket
# AF_INET = IPv4
# SOCK_DGRAM = UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server IP address and port
HOST = '127.0.0.1'
PORT = 5000

# Bind the socket to IP address and port
server_socket.bind((HOST, PORT))

print("UDP Server is waiting for messages...")

# Receive data from client
# recvfrom() returns:
# 1. Data received
# 2. Address of the sender
data, client_address = server_socket.recvfrom(1024)

# Convert bytes into string
message = data.decode()

print("Message from client:", message)
print("Client address:", client_address)

# Send response back to the client
response = "Hello from UDP Server!"

# sendto() sends data directly to the specified address
server_socket.sendto(response.encode(), client_address)

# Close the socket
server_socket.close()

print("Server closed.")
