from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()

print('The server is ready to receive...')

def handleReq():
    header = request.split('\n')
    namaFile = header[0].split()[1]

    if namaFile == '/':
        namaFile = '/index.html'

    try:
        file = open(namaFile[1:]).read()
        respone = 'HTTP/1.0 200 OK\n\n' + file

    except FileNotFoundError:
        respone = 'HTTP/1.0 404 Not Found\n\n<h1>File Not Found</h1>'

    return respone

while True:
    conn, addr = serverSocket.accept()

    request = conn.recv(1028).decode()
    respon = handleReq().encode()
    conn.sendall(respon)
    
    conn.close()
    

serverPort.close()


"""
print("Dari client:"+ sentence)
    respon = "Dari Server:"+ sentence
    connectionSocket.send(respon.encode())
"""