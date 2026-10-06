
import socket

# Create a UDP socket
# AF_INET = IPv4
# SOCK_DGRAM = UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000

# Message to send
message = "Hello from UDP Client!"

# Send message to the server
# Unlike TCP, we don't establish a connection first
client_socket.sendto(
    message.encode(),
    (SERVER_IP, SERVER_PORT)
)

print("Message sent to server.")

# Receive response from server
data, server_address = client_socket.recvfrom(1024)

# Convert bytes into string
response = data.decode()

print("Message from server:", response)

# Close the socket
client_socket.close()

print("Client closed.")