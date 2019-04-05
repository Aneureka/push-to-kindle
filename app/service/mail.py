import requests
from flask import current_app


def send(to_email, attachments=None):
    # send mail with mailgun
    # TODO: deal with attachments
    result = requests.post(
        'https://api.mailgun.net/v3/%s/messages' % current_app.config['MG_DOMAIN_NAME'],
        auth=('api', current_app.config['MG_API_KEY']),
        data={
            'from': current_app.config['MG_EMAIL_FROM'],
            'to': to_email,
            'subject': current_app.config['MG_EMAIL_SUBJECT'],
            'text': current_app.config['MG_EMAIL_TEXT']
        },
        files=[('attachment', attachments)]
    )

    if result.ok:
        return True
    else:
        print(result.text)
        return False

