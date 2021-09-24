import os
from twilio.rest import Client


def sendsms(args):
    account_sid = "AC3d66aa82a37a9bf6158a9ff308067025"
    auth_token = "9109cbd974bb2e8be2d953fa51d33cc5"
    client = Client(account_sid, auth_token)
    otp = args
    message = client.messages \
                    .create(
                        body="your OTP for login:{}".format(otp),
                        from_='+13237363902',
                        to='+918347863688'
                    )
    print("message sent successful")
