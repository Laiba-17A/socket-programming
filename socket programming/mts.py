import socket
import threading

# Function to handle communication with one client
def handle_client(client_socket, client_address):

    print(f"Client connected: {client_address}")

    while True:

        # Receive message from client
        data = client_socket.recv(1024)

        # If no data is received, client has disconnected
        if not data:
            break

        # Convert bytes to string
        message = data.decode()

        print(f"Message from {client_address}: {message}")

        # Send response back to the client
        response = "Server received: " + message
        client_socket.send(response.encode())

    # Close client's socket
    client_socket.close()

    print(f"Client disconnected: {client_address}")


# Create TCP socket
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Server IP and port
HOST = '127.0.0.1'
PORT = 5000

# Bind socket to IP and port
server_socket.bind((HOST, PORT))

# Start listening for clients
server_socket.listen(5)

print("Multithreaded TCP Server is running...")
print(f"Listening on {HOST}:{PORT}")

while True:

    # Accept a new client
    client_socket, client_address = server_socket.accept()

    # Create a new thread for this client
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    # Start the thread
    client_thread.start()

    print("Active thread count:",
          threading.active_count())