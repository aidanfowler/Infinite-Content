from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
import zmq
from PIL import Image
import io

tcp = "tcp://*:42024"
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.gpio_slowdown = 2
options.brightness = 100
options.hardware_mapping="adafruit-hat-pwm"

matrix = RGBMatrix(options = options)
print ("Matrix initialized")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(tcp)
print "server listening on " +tcp

while (True):
    message = socket.recv()
    im = Image.frombytes("RGB", (64, 32), message, "raw")
    socket.send(b"gotFrame")
    for j in range(0, 64):
        for k in range(0,32):
            cordinate=j,k
            pixelValue=im.getpixel(cordinate)
            matrix.SetPixel(j, k, pixelValue[0],pixelValue[1], pixelValue[2])