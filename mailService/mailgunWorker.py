import requests


def send_email(email, text):
    print(f"email sent to : {email} text : {text}")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox01600993de9844799722031ae524bb0b.mailgun.org/messages",
        auth=("api", "8d7d50668b45b62758e28da5572dee29-2c441066-3fbc4e33"),
        data={
            "from": "Excited User <mailgun@sandbox01600993de9844799722031ae524bb0b.mailgun.org>",
            "to": [email, "YOU@sandbox01600993de9844799722031ae524bb0b.mailgun.org"],
            "subject": "song recommendation",
            "text": text})
