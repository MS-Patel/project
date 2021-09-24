import os
from twilio.rest import Client


def sendsms(args):
    account_sid = "AC3d66aa82a37a9bf6158a9ff308067025"
    auth_token = "7bb5104ca94f6e48d4872c04b2199722"
    client = Client(account_sid, auth_token)
    otp = args
    message = client.messages \
                    .create(
                        body="your OTP for login:{}".format(otp),
                        from_='+13237363902',
                        to='+918347863688'
                    )
    print("message sent successful")
