import requests
from flask import current_app


def send_mail(to_email, files=None):
    # send mail with mailgun
    try:
        result = requests.post(
            'https://api.mailgun.net/v3/%s/messages' % current_app.config['MG_DOMAIN_NAME'],
            auth=('api', current_app.config['MG_API_KEY']),
            data={
                'from': current_app.config['MG_EMAIL_FROM_USER'],
                'to': to_email,
                'subject': current_app.config['MG_EMAIL_SUBJECT'],
                'text': current_app.config['MG_EMAIL_TEXT']
            },
            files=[('attachment', f) for f in files]
        )
        if result.ok:
            return True
        else:
            print(result.text)
            return False
    except requests.exceptions.ConnectionError as e1:
        return False
    except requests.exceptions.BaseHTTPError as e2:
        return False
