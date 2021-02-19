# import solution module
from socket import *
import sys  # In order to terminate the program


def webserver(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', port))
    serverSocket.listen(5)
    while True:
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            connectionSocket.send('\n'.encode('utf-8'))
            connectionSocket.send('HTTP/1.1 200 OK \n'.encode('utf-8'))
            connectionSocket.send("\nHTTP/1.1 200 OK \nContent-Type: text/html\r\n\r\n".encode('utf-8'))
            #connectionSocket.send('\n\n'.encode('utf-8'))

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            connectionSocket.send("\nHTTP/1.1 404 Not Found\n".encode('utf-8'))
            connectionSocket.send("\nHTTP/1.1 404 Not Found Content-Type: text/html\r\n\r\n".encode('utf-8'))
            connectionSocket.close()

            serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webserver(13331)
