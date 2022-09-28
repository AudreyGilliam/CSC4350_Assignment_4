#Audrey Gilliam
#Assignment 4 - CSC 4350
'''This program will be a simple web server that handles one HTTP request at
a time. Will accept and parse the HTTP request, get the requested file
from the server's file system, create an HTTP response message consisting of the
requested file preceded by header lines, and then send the response directly
to the client. If the requested file is not present in the server, the server
should send an HTTP "404 Not Found" message back to the client.'''


from sys import stderr
import sys
#import socket
from socket import *
import argparse 
#create a server port
serverPort = 8000
#create an instance of TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
#bind
serverSocket.bind(('', serverPort))
#listen for instructions
serverSocket.listen(1)
#print statement
print("The server is ready to receive")


while True:
    try:
        connectionSocket, addr = serverSocket.accept()

        sentence = connectionSocket.recv(1024).decode()

        #open and read file

        #look at resource and look at file system to make sure that resource exists
        #return file

        #send back HTTP header

        sentence = "HTTP/1.1 200 OK\r\n\r\n"

        #sentence = "HTTP/1.1 404 Not Found\r\n\r\n"

        #work on doing 404, have case where you find resourse
        #check for exists, if does send 200 if not send 404
        #send back 

        connectionSocket.send(sentence.encode())

        connectionSocket.close()
        
    except KeyboardInterrupt:
        sys.exit()

