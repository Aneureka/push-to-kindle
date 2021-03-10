import json
from smtplib import SMTPDataError

import requests
from flask import current_app, render_template, request

from app.service.file import create_file, read_file, remove_file
from app.service.mail import send_mail
from app.utils import convert_file_size_to_mb

from . import api


@api.route("/ping", methods=["GET"])
def ping():
    return render_template("banner.html")


@api.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        title=current_app.config["APP_NAME"],
        from_user=current_app.config["MG_EMAIL_FROM"],
        host=current_app.config["HOST"],
    )


@api.route("/files", methods=["POST", "DELETE"])
def handle_files():
    if request.method == "POST":
        file = request.files["file"]
        # validate file type
        if file is None:
            return json.dumps({"code": -2, "msg": "Missing uploaded file."})
        try:
            file_id = create_file(file)
            return json.dumps({"code": 0, "data": file_id})
        except ValueError as e:
            print(str(e))
            return json.dumps({"code": -1, "msg": str(e)})
    else:
        file_id = request.data.decode("utf-8")
        if file_id is None or file_id == "":
            return json.dumps({"code": -1, "msg": "Missing file id."})
        remove_file(file_id)
        return json.dumps({"code": 0, "data": file_id})


@api.route("/push", methods=["POST"])
def push():
    data = request.json
    to_email = data.get("email")
    file_ids = data.get("fileIds")
    if to_email is None or file_ids is None:
        return json.dumps({"code": -1, "msg": "Email and File ids are required."})
    # send emails
    files = [read_file(file_id) for file_id in file_ids]
    try:
        for file in files:
            file = [file]
            send_mail(
                to_email,
                current_app.config["MG_EMAIL_FROM"],
                current_app.config["MG_EMAIL_SUBJECT"],
                current_app.config["MG_EMAIL_TEXT"],
                file,
                current_app.config["MG_DOMAIN_NAME"],
                current_app.config["MG_API_KEY"],
            )
        return json.dumps({"code": 0})
    except requests.exceptions.RequestException as e:
        print(str(e))
        return json.dumps(
            {"code": -1, "msg": "Failed to send emails. Please try again."}
        )
    except SMTPDataError as e1:
        print(str(e1))
        return json.dumps({"code": -2, "msg": "File too large."})
