import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    # Create a socket object
    server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(host, port))

    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print('Connection established from:',addr)

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(' Received message from client:',data)

    # Send a response to the client
    response = 'Message received successfully'
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    start_server( )