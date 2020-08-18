from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb6ff1dc6393fcd5d034c40b90f78d466"
# Your Auth Token from twilio.com/console
auth_token  = "4ec8b04be4fc6a0081795dc697cb2564"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12407132509", 
    from_="+12052559796",
    body="Hello from Python!")

print(message.sid)