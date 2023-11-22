import socket

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)

    print('Server started. Listening on {}:{}'.format(*server_address))

    try:
        while True:
            print('Waiting for a file to be uploaded...')
            data, client_address = server_socket.recvfrom(1024)
            filename = data.decode()
            print('Received request to upload file:', filename)

            # Open a new file for writing
            with open(filename, 'wb') as file:
                while True:
                    data, client_address = server_socket.recvfrom(1024)
                    if len(data) == 0:
                        break
                    file.write(data)

            print('File', filename, 'has been uploaded successfully.')

    except KeyboardInterrupt:
        print('Server stopped by the user.')

    finally:
        # Close the socket
        server_socket.close()

if __name__ == '__main__':
    main()
