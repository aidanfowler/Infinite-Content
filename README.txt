Infinite Content - Aidan Lincoln 
ITP Thesis

- This repo contains a processing server + client which takes in syphon input from max/msp or touchdesigner (todo isadora) and sends UDP byte arrays to the UDP server running on the raspberry pi
- Rpi code relies on hzeller rpi rgb matrix library (https://github.com/hzeller/rpi-rgb-led-matrix)

- I left in the old server and client files becasue they work and might be usefull if you want to use ZMQ.
- SyphoneClientUDPServer (grab syphon data from touch / max msp / isadora etc or just the processing canvas and sends udp frames to RPi)
- matrixServer.py - running on the pi to be used with processing sketch that receives udp byte arrays and converts them into pixels
- matrixClient.py - middleware that I initially had receiving UDP from processing and sending ZMQ to the pi
- matrixClientZMQ.py - processing a gif with Pillow Image library into byte array and sending via zmq to 
- matrixServerZMQ.py - receives a zmq message and converts byte array into image and writes to led matrix.
