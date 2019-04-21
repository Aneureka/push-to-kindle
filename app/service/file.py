import os
import glob
import uuid
from flask import current_app
from app.utils import translate


def create_file(file):
    origin_filename = file.filename.encode('ascii', 'replace').decode('utf-8')
    origin_filename = file.filename
    _, file_type = os.path.splitext(origin_filename)
    if file_type not in current_app.config['ACCEPTED_FILE_TYPES']:
        raise ValueError('Not supported file type.')
    file_id = str(uuid.uuid4())
    filename = os.path.join(current_app.config['UPLOAD_FOLDER'], '%s.%s' % (origin_filename, file_id))
    if not os.path.exists(filename):
        file.save(filename)
    return file_id


def remove_file(file_id):
    filename = _get_filename(file_id)
    if filename:
        os.remove(filename)


def read_file(file_id):
    filename = _get_filename(file_id)
    origin_filename = os.path.splitext(filename)[0]
    origin_filename = origin_filename.split('/')[-1]
    # translate to English
    origin_filename = translate(origin_filename)
    if filename:
        with open(filename, 'rb') as f:
            return origin_filename, f.read()
    return None


def _get_filename(file_id):
    filenames = glob.glob(os.path.join(current_app.config['UPLOAD_FOLDER'], '*.%s' % file_id))
    if filenames:
        return filenames[0]
    else:
        return ''

