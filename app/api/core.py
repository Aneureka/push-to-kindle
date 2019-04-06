from flask import request, render_template, current_app
import requests
import json

from . import api
from app.service.mail import send_mail
from app.service.file import create_file, remove_file, read_file


@api.route('/ping', methods=['GET'])
def ping():
    return 'Ping successfully!'


@api.route('/test_mail', methods=['GET'])
def test_mail():
    send_mail(to_email='972579500@qq.com')
    return 'Send email successfully!'


@api.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', title=current_app.config['APP_NAME'], from_user=current_app.config['MG_EMAIL_FROM'], host=current_app.config['HOST'])
    else:
        pass


@api.route('/files', methods=['POST', 'DELETE'])
def handle_files():
    if request.method == 'POST':
        file = request.files['file']
        # validate file type
        if file is None:
            return json.jumps({'code': -2, 'msg': 'Missing uploaded file.'})
        try:
            file_id = create_file(file)
            return json.dumps({'code': 0, 'data': file_id})
        except ValueError as e:
            return json.dumps({'code': -1, 'msg': str(e)})
    else:
        file_id = request.data.decode('utf-8')
        if file_id is None or file_id == '':
            return json.dumps({'code': -1, 'msg': 'Missing file id.'})
        remove_file(file_id)
        return json.dumps({'code': 0, 'data': file_id})


@api.route('/push', methods=['POST'])
def push():
    data = request.json
    to_email = data.get('email')
    file_ids = data.get('fileIds')
    if to_email is None or file_ids is None:
        return json.dumps({'code': -1, 'msg': 'Email and File ids are required.'})
    # send emails
    files = [read_file(file_id) for file_id in file_ids]
    try:
        send_mail(to_email, files)
        for file_id in file_ids:
            remove_file(file_id)
        return json.dumps({'code': 0, 'data': file_ids})
    except requests.exceptions.RequestException as e:
        print(str(e))
        return json.dumps({'code': -1, 'msg': 'Failed to send emails. Please try again.'})
