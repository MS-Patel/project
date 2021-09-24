import os
from twilio.rest import Client


def sendsms(args):
    account_sid = "your sid here"
    auth_token = "your token here"
    client = Client(account_sid, auth_token)
    otp = args
    message = client.messages \
                    .create(
                        body="your OTP for login:{}".format(otp),
                        from_='+13237363902',
                        to='+918347863688'
                    )
    print("message sent successful")
