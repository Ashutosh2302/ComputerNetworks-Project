import socket

d=socket.socket()
d.bind(('localhost',1000))
d.listen(1)
while True:
    cd, addr = d.accept()
    print("Connected with ", addr)


    cd.send(bytes("Connected with Doctor",'utf-8'))
    while True:
            message=input("Enter message for patient: ")
            cd.send(bytes(message, 'utf-8'))
            patient_message=cd.recv(1024).decode()
            print("Patient: ",patient_message)
    cd.close()
    break
