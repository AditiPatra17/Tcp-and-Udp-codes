import socket

def server_program():
    #get the hostname
    host = socket.gethostname()
    port = 5000
    
    server_socket = socket.socket()
    
    server_socket.bind((host,port))
    
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: "+ str(address))
    while True:
        #receive data stream. It wont accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            #if data is not recieved break
            break
        print("from connected user: " +str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()
    
if __name__ == '__main__':
    server_program()