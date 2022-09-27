#Audrey Gilliam
#Assignment 4 - CSC 4350
'''This program will be a simple web server that handles one HTTP request at
a time. Will accept and parse the HTTP request, get the requested file
from the server's file system, create an HTTP response message consisting of the
requested file preceded by header lines, and then send the response directly
to the client. If the requested file is not present in the server, the server
should send an HTTP "404 Not Found" message back to the client.'''

'''USE A DIFFERENT BLOCK OF TEXT TO DESCRIBE PROGRAM'''


#import socket
from socket import *
#requests library
import requests
#create a server port
serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")



'''while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()

    connectionSocket.send(sentence.upper().encode())

    connectionSocket.close()'''

#r = requests.get('http://codesource.io/')

#print(r.status_code)
