# Download the Python helper library from twilio.com/docs/python/install
import os
import time
from twilio.rest import Client

file = open("/home/lucas/Lucas/twilio/text.txt", "r")
text = file.read().split("\n")
file.close()


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Make API calls here...
for i in text:
    message = client.messages.create(
                                     body=i,
                                     from_='whatsapp:+14155238886',
                                     to='whatsapp:+5492613893139'
                                    )
    time.sleep(1)
