"""
AUTOMAILER by...
 _       __   __      __ _  __   ____ __   __
| |     /  \  \ \    / /| |/ /  |__ / \ \ / /
| |__  | () |  \ \/\/ / |   <    |_ \  \   / 
|____|  \__/    \_/\_/  |_|\_\  |___/   |_|  

[+] Are you annoyed with the tedious task of sending repetitive daily emails? Use Automailer!
 
This script can be used to automatically send scheduled emails to any email of your choosing. 
Since I was not planning on releasing this publicly, a few of the variables are hardcoded. 
I will change the variables to take user-input in a future release, or you can change them until then with this source code.
Once you've set your variables to your liking, just throw it onto a server, run it and you're good to go. :)


Required PIP packages to be installed:

Schedule: https://pypi.org/project/schedule/
Twilio: https://pypi.org/project/twilio/

or use

"pip install -r requirements.txt" (Paste in CLI)


Enjoy :)
"""



import smtplib
import datetime
import schedule #https://pypi.org/project/schedule/
import subprocess
import time
from twilio.rest import Client #https://pypi.org/project/twilio/



#Twilio Variables
account_sid = "ENTER TWILIO ACCOUNT ID HERE"
auth_token = "ENTER TWILIO AUTH TOKEN HERE"
client = Client(account_sid, auth_token)



#SMTP Variables
sender_email = "INSERT@EMAIL.COM"
password = "INSERT SMTP PASSWORD HERE"
receiver_email = ["INSERT@EMAIL.COM", "INSERT2@EMAIL.COM"]
message = "INSERT EMAIL MESSAGE HERE" 
recipients = '\n'.join(receiver_email)



#Data Variables
date = datetime.datetime.now()
currentDate = date.strftime("%B %d %Y, %I:%M:%S%p %Z")
print(date.strftime("%B %d %Y, %I:%M:%S%p EST"))

subprocess.call(['cls'],shell=True)
print('Waiting for execution time...')



#Mailing function
def send_email(): 

    subprocess.call(['cls'],shell=True)
    server = smtplib.SMTP('smtp.gmail.com', 587) #Change SMTP client here.
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    print("Login Successful.")
    for receiver in receiver_email: 
        server.sendmail( sender_email, receiver, "INSERT SUBJECT HERE. ex: Subject: ..." + message )
        print("Email has been sent to " + receiver)
    server.quit()
    subprocess.call(['cls'],shell=True)
    print('Waiting for execution time...')
    
    
    
    #Creates log of when check-in was sent.
    f = open("logs.txt", "a")
    f.write("Check in sent for: " + currentDate + "\n\n")
    f.close()
    
    
    
    #Sends a text notification when email was sent.
    txt = client.messages.create(
    to="INSERT TO NUMBER HERE. ex. +1234567890", 
    from_="INSERT FROM NUMBER HERE. ex. +1234567890",
    body="INSERT TEXT MSG BODY HERE.")
    print(txt)

    
    
#Schedule Functions
def off_day():
    print("Today is Sunday, enjoy your off day! :)")

#Sends email on scheduled days
schedule.every().monday.at("00:00").do(send_email)
schedule.every().tuesday.at("00:00").do(send_email)
schedule.every().wednesday.at("00:00").do(send_email)
schedule.every().thursday.at("00:00").do(send_email)
schedule.every().friday.at("00:00").do(send_email)
schedule.every().saturday.at("00:00").do(send_email)
schedule.every().sunday.do(off_day())



#Keeps script running.
while True:
    schedule.run_pending()
    time.sleep(1)
