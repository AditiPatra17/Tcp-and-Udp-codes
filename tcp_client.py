import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    #Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to server
    client_socket.connect((host,port))

    #Send a message to the server
    message = 'Hello, server!'
    client_socket.send(message.encode())

    #Receive the server's response
    response = client_socket.recv(1024).decode()
    print('Response from server:', response)

    #Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()