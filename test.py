from twilio.rest import Client

account_sid = "ACb6ff1dc6393fcd5d034c40b90f78d466"
auth_token = "4ec8b04be4fc6a0081795dc697cb2564"
client = Client(account_sid, auth_token)

txt = client.messages.create(
    to=input("Enter receivers phone number: " + "+1"), 
    from_="+12052559796",
    body=input(str("Enter your message: ")))
    
print("Message sent ")