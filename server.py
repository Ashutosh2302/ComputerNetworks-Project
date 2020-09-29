import smtplib
import socket
import mysql.connector
socket.getaddrinfo('localhost', 8080)
import pickle
mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='server')
cur=mydb.cursor()

s = socket.socket()
print('Socket Created')
hotspots = ['delhi', 'noida', 'mumbai']

s.bind(('localhost', 9999))
s.listen(2)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    print("Connected with ", addr)

    file = open('advisory.txt', 'w')
    file.write("******Coronavirus Advisory******\n\n\n")
    file.write("Government has decided to put the entire country in lockdown for 3 weeks amid coronavirus threat\n\n")
    file.write("Below mentioned places are the coronavirus hotspots of the country\n\n")
    h = str(hotspots)
    file.write(h)
    file.write("\n\nIf you live in or nearby these places please take serious precautions.\n\n")
    file.write("\n\nDo's\n1. Wash hand regularly\n2. Cover your nose and mouth while sneezing  and coughing\n3. Avoid public gatherings")
    file.write("\n\nDont's\n1. Touch your nose, eyes and mouth\n2. Spit in public")
    file.write('\n\nPlease use this application as it could solve many of your problems')
    file.write("\n\nStay home! Stay Safe\n\n")

    print("Advisory Created!")

    file.close()
    file = open('advisory.txt', 'rb')
    file_data = file.read(1024)
    c.send(file_data)
    print("Advisory Sent to Client")
    choice = c.recv(1024).decode()

    if int(choice) == 4:
        city = c.recv(1024).decode()
        query="SELECT * FROM covid19_data WHERE city=%s"
        try:
            cur.execute(query,(city,))
            result=cur.fetchall()
        except:
            print("Error")
        else:
            result=list(result)
            y = str(result)
            c.send(y.encode())
    if int(choice) == 3:

            data = c.recv(2048)
            data = data.decode('utf-8')
            data = eval(data)
            '''name = c.recv(1024).decode()
            city = c.recv(1024).decode()
            phone = c.recv(1024).decode()
            email = c.recv(1024).decode()'''
            details=(data[0],data[1],data[2],data[3])

            content = "\nCOVID-19 checkup confirmation\n\nOur team of Doctors will contact you and check your symptoms, Due to limited number of test kits available,if you show symptoms of " \
                          "COVID-19 then only doctors will collect your sample and test it " \
                          "\n\nThankyou \n\nMinistry of Health and Family Affairs"
            sender = "ashuabc999@gmail.com"
            recipient = data[3]

            password = "marshmellow"
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.starttls()
            mail.login(sender, password)
            try:
                mail.sendmail(sender, recipient, content)
            except smtplib.SMTPRecipientsRefused:
                print("The recipient address {recipient} is not a valid")
                msg = "False"
                c.send(bytes(msg, 'utf-8'))
            else:
                print("sent email to ", recipient)
                msg="True"
                c.send(bytes(msg, 'utf-8'))
                query="INSERT INTO testing VALUES(%s,%s,%s,%s)"
                try:
                    cur.execute(query,details)
                except:
                    print("Error occurred")
                else:
                    print("Data saved!")
                    mydb.commit()
    if  int(choice) == 5:
        city = c.recv(1024).decode()
        query = "SELECT * FROM essential_needs WHERE city=%s"
        try:
            cur.execute(query, (city,))
            result = cur.fetchall()
        except:
            print("Error")
        else:
            result = list(result)
            y = str(result)
            c.send(y.encode())
           # print(result)
    if int(choice) == 6:
        query = "Select * FROM quiz "
        try:
            cur.execute(query)
            result = cur.fetchall()
        except:
            print("Error")
        else:
            print(result)
            result = list(result)
            y = str(result)
            c.send(y.encode())
c.close()
