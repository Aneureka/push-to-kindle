import os
import glob
import uuid
import re
from flask import current_app
from app.utils import translate


def create_file(file):
    origin_filename = file.filename.encode('ascii', 'replace').decode('utf-8')
    origin_filename = file.filename
    core_filename, file_type = os.path.splitext(origin_filename)
    if file_type not in current_app.config['ACCEPTED_FILE_TYPES']:
        raise ValueError('Not supported file type.')
    if file_type in current_app.config['TRANSFER_FILE_TYPES']:
        file_type = '.html'
    file_id = str(uuid.uuid4())
    filename = os.path.join(current_app.config['UPLOAD_FOLDER'], '%s%s.%s' % (core_filename, file_type, file_id))
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
    pattern = re.compile('[\u00A1-\uFFFF]')
    core_filename, file_type = os.path.splitext(origin_filename)
    # check if filename contains utf-8 characters
    if pattern.search(core_filename) is not None:
        core_filename = translate(core_filename)
    origin_filename = core_filename + file_type
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

