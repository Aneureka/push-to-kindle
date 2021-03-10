import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPDataError

import requests
from flask import app, current_app


def send_mail(to_email, from_email, subject, text, files, domain_name, password):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.attach(MIMEText(text, _charset="utf-8"))
    for file in files:
        file_name, file_content = file
        print(file_name)
        part = MIMEApplication(file_content)
        part.add_header(
            "Content-Disposition", "attachment", filename=("gb18030", "", file_name)
        )
        msg.attach(part)
    s = smtplib.SMTP("smtp.mailgun.org", 587)
    s.login("postmaster@%s" % domain_name, password)
    try:
        s.sendmail(msg["From"], msg["To"], msg.as_string())
    except SMTPDataError as e:
        raise e
    finally:
        s.close()


def send_mail_via_api(
    to_email, from_email, subject, text, files, domain_name, auth_api
):
    # send mail with mailgun
    try:
        response = requests.post(
            "https://api.mailgun.net/v3/%s/messages" % domain_name,
            auth=("api", auth_api),
            data={"from": from_email, "to": to_email, "subject": subject, "text": text},
            files=[("attachment", f) for f in files],
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e1:
        raise e1
    except requests.exceptions.RequestException as e2:
        raise e2
    except Exception as e:
        raise e
