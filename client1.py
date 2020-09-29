import socket
c=socket.socket()
c.connect(('localhost',9999))

def menu():
    print("1. Chat with a doctor")
    print("2. Chat with COVID-19 emergency helpline service")
    print("3. Get tested for COVID-19 ")
    print("4. Check how safe is your city")
    print("5. Essential needs stores information")
    print("6. How well you know about COVID-19?")
    choice=int(input("Enter your choice- "))
    return choice
file=open('adv1.txt','wb')
file_data=c.recv(1024)
file.write(file_data)
file.close()
print("Advisory Received")

choice=menu()
if choice==1:
    c.send(bytes(str(choice), 'utf-8'))
    c.close()
    cd = socket.socket()
    cd.connect(('localhost', 1000))

    doctor_message=cd.recv(1024).decode()
    print("Server: ",doctor_message)
    while True:
        doctor_message = cd.recv(1024).decode()
        print("Doctor: ", doctor_message)
        message=input("Enter message for doctor: ")
        cd.send(bytes(message, 'utf-8'))
if choice==2:
    c.send(bytes(str(choice), 'utf-8'))
    c.close()
    ce = socket.socket()
    ce.connect(('localhost', 2000))

    helpline_message=ce.recv(1024).decode()
    print("Server: ",helpline_message)
    while True:
        helpline_message = ce.recv(1024).decode()
        print("Emergency_service: ", helpline_message)
        message=input("Enter message for COVID19 emergency: ")
        ce.send(bytes(message, 'utf-8'))
if choice==4:

    c.send(bytes(str(choice), 'utf-8'))
    city=input("Enter your city")
    c.send(bytes(city, 'utf-8'))
    data = c.recv(1024)
    data = data.decode('utf-8')
    data = eval(data)
    list=['city: ','zone-type: ','COVID19 cases: ', 'Recovered: ','Decreased: ']
    k=0
    r=0
    o=0
    g=0
    if data:
        for e in data[0]:
            print(list[k],e)
            k+=1
            if e=='red':
                r=1
            if e=='orange':
                o=1
            if e=='green':
                g=1
        if r==1:
            print("Your region is high risk zone! connect with doctors and COVID-19 helpline for more information")
        if o==1:
            print("Your region is less risk zone! connect with doctors and COVID-19 helpline for more information")
        if g==1:
            print("Your region is COVID-19 free zone! connect with doctors and COVID-19 helpline for more information")
    else:
        print("Your region is COVID-19 free zone! connect with doctors and COVID-19 helpline for more information")
if choice==3:
    #print("NOTE: Please consult with doctor before booking appointment")
    #x=input("want to continue with booking? (y/n)")
   # if x=='y':
        c.send(bytes(str(choice), 'utf-8'))
        name=input("Enter your Name")
        city=input("Enter your city")
        phone=input("Enter your contact no")
        email=input("Enter your email ID")
        result=(name,city,phone,email)
        result = list(result)
        y = str(result)
        c.send(y.encode())
        '''c.send(bytes(name, 'utf-8'))
        c.send(bytes(city, 'utf-8'))
        c.send(bytes(phone, 'utf-8'))
        c.send(bytes(email, 'utf-8'))'''
        msg = c.recv(1024).decode()
        if msg=="True":
            print("Please check your email")
        if msg=="False":
            print("Wrong email address")
if choice==5:
    c.send(bytes(str(choice), 'utf-8'))
    city=input("Enter your city: ")
    c.send(bytes(city, 'utf-8'))
    data = c.recv(1024)
    data = data.decode('utf-8')
    data = eval(data)
    list=['City','Store Type','Home Delivery', 'Contact no']
    for e in list:
        print(e, end='      ')
    for item in data:
        print()
        for e in item:
            print(e,end='        ')

if choice==6:
    score=0
    inans=[]
    o=0
    z=0
    d=dict()
    c.send(bytes(str(choice), 'utf-8'))
    data = c.recv(2048)
    data = data.decode('utf-8')

    data=eval(data)
    list=[]
    for item in data:
        print()
        print("Question no. ",item[0])
        print(item[1])
        print("1. ", item[2])
        print("2. ", item[3])
        print("3. ", item[4])
        print("4. ", item[5])
        ans=int(input("Enter your answer: "))
        if item[6] == ans:
            score = score + 1
        else:
            d[item[0]] = item[item[6] + 1]
            z=z+1
            inans.append(item[ans + 1])
    print()
    print("            Your Score-", score, "out of 6")
    if score<4:
        print("You need to gain more knowledge of COVID-19")
    else:
        print("Well done!")
    if z>0:
            print("Incorrect Answers- ")
            print()
            for a, b in d.items():
                print("Question. ", a)
                print("Correct Answer: ", b)
                print("Your Answer:    ", inans[o])
                o += 1
                print()
c.close()
