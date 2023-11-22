import socket

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

def send_file(filename):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT}")

        # Send the filename to the server
        client_socket.send(filename.encode())
        print(f"[*] Sent filename: {filename}")

        # Open the file in read mode
        with open(filename, 'rb') as file:
            # Read the file in chunks and send them to the server
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.sendall(data)

    finally:
        # Close the connection
        client_socket.close()
        print("[*] File transfer complete.")

# Run the client
if __name__ == '__main__':
    filename = input("Enter the filename: ")
    send_file(filename)
