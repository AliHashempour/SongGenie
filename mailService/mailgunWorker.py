import os
from dotenv import load_dotenv
import requests

load_dotenv()


def send_email(email, text):
    print(f"email sent to : {email} text : {text}")
    return requests.post(
        f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
        auth=("api", os.getenv('MAILGUN_API_KEY')),
        data={
            "from": os.getenv('MAILGUN_FROM'),
            "to": [email, f"ali@{os.getenv('MAILGUN_DOMAIN')}"],
            "subject": "song recommendation",
            "text": text
        }
    )
