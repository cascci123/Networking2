# import socket module
from socket import *
import sys  # In order to terminate the program


def webserver(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', port))
    serverSocket.listen(5)
    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

            #for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("File Not Found".encode())
            connectionSocket.close()

        serverSocket.close()
        sys.exit()


if __name__ == "__main__":
    webserver(13331)
