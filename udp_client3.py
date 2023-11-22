import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Server address and port
    server_address = ('localhost', 5000)
    
    # Prompt the user to enter the filename
    filename = input('Enter the filename to upload: ')
    
    # Send the filename to the server
    client_socket.sendto(filename.encode(), server_address)
    
    # Open the file to be uploaded
    try:
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                # Send data to the server
                client_socket.sendto(data, server_address)
        
        print('File', filename, 'has been uploaded successfully.')
    
    except FileNotFoundError:
        print('File not found:', filename)
    
    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()
