import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

def receive_file():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    # Receive the filename from the client
    filename = client_socket.recv(BUFFER_SIZE).decode()
    print(f"[*] Received filename: {filename}")

    # Open the file in write mode
    with open(filename, 'wb') as file:
        while True:
            # Receive data from the client
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            # Write received data to the file
            file.write(data)

    # Close the connection
    client_socket.close()
    server_socket.close()
    print("[*] File transfer complete.")

# Run the server
if __name__ == '__main__':
    receive_file()
