# CSC4350_Assignment_4

Simple we server that handles one HTTP request at a time

Should accept and parse the HTTP request, get the requested
file from the server's file system, create an HTTP response
message consisting of the requested file preceded by header
lines, and then send the response directly to the client.
If the requested file is not present int he server, the server
should send and HTTP "404 Not Found" message back to the client
