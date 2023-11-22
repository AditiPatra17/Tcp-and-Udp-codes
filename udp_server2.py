import socket

localP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytestoSend = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localP, localPort))
print("UDP server up and listening")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client: {}".format(message.decode())
    clientP = "Client IP Address: {}".format(address)

    print(clientMsg)
    print(clientP)

    response = input("-> ")
    UDPServerSocket.sendto(str.encode(response), address)
