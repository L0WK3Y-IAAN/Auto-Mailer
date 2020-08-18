# from win10toast import ToastNotifier
import smtplib
import datetime
import schedule 
import subprocess
import time
#Add Twilio text notification when email is sent

sender_email = "l0wk3y@iaansec.net"
password = "sgpprfnmzppmgrum"
receiver_email = ["l0wk3y@iaansec.net", "jsfakfilms@gmail.com"]
message = "Good morning, \nI am emailing you to check in for the day.\n\nJonathan Suttle." 





subprocess.call(['cls'],shell=True)
print('Waiting for execution time...')

def send_email():
    try:
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
        
    except:
        print("Mailing function failed...")


schedule.every().day.at("04:33").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
