/**
Aidan Fowler
Infinite Content Thesis
UDP Server + Syphon Client
Pull in content from MAX/MSP / TouchDesigner / Processing canvas
Send RGB24 byte array through UDP to python server which unpacks and sends to Raspberry Pi through ZeroMQT protocol
TODO: remove need for python server and just use processing to send straight UDP if possible
*/

import hypermedia.net.*;
import codeanticode.syphon.*;

SyphonClient syphonClient;
boolean turnOnSyphon = true;
UDP udpServer;
byte[] bytes = new byte[448*32*3];
String ip = "192.168.10.2";  // the remote IP address
int port = 51000;    // the destination port
PGraphics canvas;

void setup() {
  size(448,32,P3D);
  frameRate(33);
  colorMode(RGB, 255, 255, 255);
  
  if(turnOnSyphon){
    println("Available Syphon servers:");
    println(SyphonClient.listServers());
    println("Connecting Syphon Client");
    //syphonClient = new SyphonClient(this, "Max", "Jitter");
    syphonClient = new SyphonClient(this, "TouchDesigner", "TDSyphonSpout");
  }
    
  println("Initializing UDP Server");
  udpServer = new UDP( this );// create a new datagram connection (dont care about getting messages back)
  //udpServer.log( true );
  
}

//process events
void draw() {
  //every few seconds print the frame rate
  if(frameCount % 100 == 0){
    println("Framerate: "+frameRate);
  }
  if (turnOnSyphon && syphonClient.newFrame()) {
    canvas = syphonClient.getGraphics(canvas);
    image(canvas, 0, 0, width, height);    
  }
  else if (!turnOnSyphon){
    background(50+mouseX/2,mouseY*6,255);
  }
  loadPixels(); //load canvas pixels into int array
  for(int i=0; i<pixels.length; i++) { //convert pixels into RGB byte array
    int c = pixels[i];
    bytes[i*3] = (byte)(c >> 16 & 0xFF);
    bytes[i*3+1] = (byte)(c >> 8 & 0xFF);
    bytes[i*3+2] = (byte)(c & 0xFF);
  }
  //println("pixels size "+pixels.length);
  //println("message size "+bytes.length);
  //println("ip: "+ip+" port: "+port);
  udpServer.send( bytes, ip, port );
}
