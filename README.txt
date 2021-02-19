Infinite Content - Aidan Lincoln 
ITP Thesis

- This repo contains a processing server + client which takes in syphon input from max/msp or touchdesigner (todo isadora) and sends UDP byte arrays to the UDP server running on the raspberry pi

- The server files should go on the pi and relies on hzellers rpi rgb matrix library (https://github.com/hzeller/rpi-rgb-led-matrix). The server implements UDP
- The matrix client file is what I used for testing before getting the processing code directly connected to the pi with udp. It receives udp from processing and sends zmq to the pi.
- The clientZmq is what was implemented before using UDP
- Both client files goes with the zmqServer file
- The client that works with the current server is in the processing sketch
