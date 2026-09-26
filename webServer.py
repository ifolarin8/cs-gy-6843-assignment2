# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)
  


  while True:
    #Establish the connection
    
    # print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')
      
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Server: MyWebServer\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      for i in f: #for line in file
          outputdata += i

      f.close() # close the file
      connectionSocket.send(outputdata)
      connectionSocket.close()
      

      

      connectionSocket.send(outputdata)

      
        
    
    except Exception as e:
     error_response = b"HTTP/1.1 404 Not Found\r\n"
     error_response += b"Server: MyWebServer\r\n"
     error_response += b"Content-Type: text/html; charset=UTF-8\r\n"
     error_response += b"Connection: close\r\n"
     error_response += b"\r\n"
     error_response += b"<HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD>"
     error_response += b"<BODY>404: File Not Found</BODY></HTML>"
      
     connectionSocket.send(error_response)
     connectionSocket.close() # closing the connection socket

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

