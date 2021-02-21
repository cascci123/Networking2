# import socket module
from socket import *
import sys  # In order to terminate the program


def webserver(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', port))
    serverSocket.listen(1)
    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            connectionSocket.sendall("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            connectionSocket.sendall("HTTP/1.1 404 Not Found\r\n\r\n404 Not Found\r\n".encode())
            connectionSocket.close()

        serverSocket.close()
        sys.exit()


if __name__ == "__main__":
    webserver(13331)
