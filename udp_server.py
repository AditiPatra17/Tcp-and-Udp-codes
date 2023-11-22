import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print("UDP server up and listening")
di = {'21BIT0086':'Advay','21BIT0092':'Pratham','21BIT0096':'Aditya','21BIT0125':'Aditi'}
while(True):
    name,addr1 = UDPServerSocket.recvfrom(bufferSize)
    pwd,addr1 = UDPServerSocket.recvfrom(bufferSize)
    name = name.decode()
    pwd = pwd.decode()
    msg = ''
    if name not in di:
        msg = 'name does not exists'
        flag = 0
    for i in di:
        if i == name:
            if di[i] == pwd:
                msg = "pwd match"
                flag = 1
            else:
                msg = "pwd wrong"
        bytesToSend = str.encode(msg)
        UDPServerSocket.sendto(bytesToSend,addr1)