import socket
print("Aditi Patra 21BIT0125")
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1",5005)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend,serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0])
print(msg)