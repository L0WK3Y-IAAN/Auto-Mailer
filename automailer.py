# from win10toast import ToastNotifier
import smtplib
import datetime
import schedule 
import subprocess
import time
from twilio.rest import Client


#Twilio Variables
account_sid = "ACb6ff1dc6393fcd5d034c40b90f78d466"
auth_token = "4ec8b04be4fc6a0081795dc697cb2564"
client = Client(account_sid, auth_token)

#SMTP Variables
sender_email = "l0wk3y@iaansec.net"
password = "sgpprfnmzppmgrum"
receiver_email = ["l0wk3y@iaansec.net", "jsfakfilms@gmail.com"]
message = "Good morning, \nI am emailing you to check in for the day.\n\nJonathan Suttle." 
recipients = '\n'.join(receiver_email)

#Data Variables
date = datetime.datetime.now()
currentDate = date.strftime("%B %d %Y, %I:%M:%S%p %Z")
print(date.strftime("%B %d %Y, %I:%M:%S%p EST"))



subprocess.call(['cls'],shell=True)
print('Waiting for execution time...')

def send_email(): #Mailing function

    subprocess.call(['cls'],shell=True)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    print("Login Successful.")
    for receiver in receiver_email: 
        server.sendmail( sender_email, receiver, "Subject:Checking in | Jonathan Suttle\n" + message )
        print("Email has been sent to " + receiver)
    server.quit()
    subprocess.call(['cls'],shell=True)
    print('Waiting for execution time...')
    
    #Creates log of when check-in was sent.
    f = open("logs.txt", "a")
    f.write("Check in sent for: " + currentDate + "\n\n")
    f.close()
    
    #Sends a text notification when check-in was sent.
    txt = client.messages.create(
    to="+12407132509", 
    from_="+12052559796",
    body="MorningStar check in sent for: " + currentDate + "\n\n Recipients: \n" + recipients)
    print(txt)

def off_day():
    print("Today is Sunday, enjoy your off day! :)")


schedule.every().monday.at("00:00").do(send_email)
schedule.every().tuesday.at("00:00").do(send_email)
schedule.every().wednesday.at("00:00").do(send_email)
schedule.every().thursday.at("00:00").do(send_email)
schedule.every().friday.at("00:00").do(send_email)
schedule.every().saturday.at("00:00").do(send_email)
schedule.every().sunday.do(off_day)

while True:
    schedule.run_pending()
    time.sleep(1)
