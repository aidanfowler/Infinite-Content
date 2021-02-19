from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import socket

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.gpio_slowdown = 2
options.brightness = 100
options.hardware_mapping="adafruit-hat-pwm"

matrix = RGBMatrix(options = options)
print ("Matrix initialized")

localIP     = "192.168.10.2"
localPort   = 51000
bufferSize  = 43008 #for 7 led screens 448x32x3

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP Server Listening For Content On Port: ",localPort)

while(True):
    # Listen for incoming datagrams
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    #address = bytesAddressPair[1]
    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    #print(len(message))
    im = Image.frombytes("RGB", (448, 32), message, "raw")
    for j in range(0, 64):
        for k in range(0,32):
            cordinate=j,k
            pixelValue=im.getpixel(cordinate)
            matrix.SetPixel(j, k, pixelValue[0],pixelValue[1], pixelValue[2])




