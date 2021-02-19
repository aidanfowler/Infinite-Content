from PIL import Image
import zmq
tcp = "tcp://192.168.10.2:42024"
from time import sleep

import socket

localIP     = "192.168.10.1"
localPort   = 51000
bufferSize  = 6144

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


print("Connecting to matrix server")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(tcp)

try:
    #send gif 10 times
    for repeat in range(0,100):
      im = Image.open("./DoubleRainbow.gif")
      print("sending gif stream from client through ",tcp)
      for frame in range(0,im.n_frames):
          im.seek(frame)
          frame = im.convert("RGB")
          frameToSend = frame.tobytes("raw")
          #print("expected frame size:6144, actual frame size:",len(frameToSend))
          socket.send(frameToSend)
          message = socket.recv()
          #because the gif is too fast (wooooooooo shouldnt be rendering issues)
          sleep(.02)
      
except EOFError:
    print("done")
    pass



