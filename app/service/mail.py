import requests
from flask import current_app
from flask import app
import time

def send_mail(to_email, from_email, subject, text, files, domain_name, auth_api):
    # send mail with mailgun
    # try:
    response = requests.post(
        'https://api.mailgun.net/v3/%s/messages' % domain_name,
        auth=('api', auth_api),
        data={
            'from': from_email,
            'to': to_email,
            'subject': subject,
            'text': text
        },
        files=[('attachment', f) for f in files]            
    )
    # response.raise_for_status()
    # except requests.exceptions.HTTPError as e1:
    #     print(e1)
    #     raise e1
    # except requests.exceptions.RequestException as e2:
    #     print(e2)
    #     raise e2
    # except Exception as e:
    #     print(e)