import socket

e=socket.socket()
e.bind(('localhost',2000))
e.listen(1)
while True:
    ce, addr = e.accept()
    print("Connected with ", addr)


    ce.send(bytes("Connected with COVID19 Emergency service",'utf-8'))
    while True:
            message=input("Enter message for client: ")
            ce.send(bytes(message, 'utf-8'))
            client_message=ce.recv(1024).decode()
            print("Client: ",client_message)
    cd.close()
    break
