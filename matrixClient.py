from PIL import Image
import zmq
from time import sleep
import socket

tcp = "tcp://192.168.10.2:42024"
localIP     = "192.168.10.1"
localPort   = 51000
bufferSize  = 43008 #for 7 led screens 64x32x3

print("\n")
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP Server Listening For Content")

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(tcp)
print("Matrix Client Opened")

while(True):
    # Listen for incoming datagrams
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    #print(clientMsg)
    #print(len(message))
    socket.send(message)
    message = socket.recv()
    #because the gif is too fast (wooooooooo shouldnt be rendering issues)
    #sleep(.02)




