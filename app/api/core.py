from flask import request, render_template, current_app
import os
import uuid
import shutil
import json
import time

from . import api
from app.service import mail


@api.route('/ping', methods=['GET'])
def ping():
    return 'Ping successfully!'


@api.route('/test_mail', methods=['GET'])
def test_mail():
    mail.send(to_email='972579500@qq.com')
    return 'Send email successfully!'


@api.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', title=current_app.config['APP_NAME'], host=current_app.config['HOST'])
    else:
        pass


@api.route('/files', methods=['POST', 'DELETE'])
def handle_files():
    if request.method == 'POST':
        file = request.files['file']
        # validate file type
        if '.' not in file.filename or file.filename.split('.')[-1] not in current_app.config['ACCEPTED_FILE_TYPES']:
            return json.dumps({'code': -1, 'msg': 'Not supported file type.'})
        file_id = str(uuid.uuid4())
        filename = os.path.join(current_app.config['UPLOAD_FOLDER'], file_id, file.filename)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        file.save(filename)
        return json.dumps({'code': 0, 'data': file_id})
    else:
        file_id = request.data.decode('utf-8')
        file_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], file_id)
        if os.path.exists(file_dir):
            shutil.rmtree(file_dir)
        return json.dumps({'code': 0, 'data': file_id})


@api.route('/push', methods=['POST'])
def push():
    data = request.json
    time.sleep(10)
    return json.dumps({'code': 0})

