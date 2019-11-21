FROM python:latest

LABEL maintainer=Yinr<yinr@yinr.cc>

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV LANG='en_US.UTF-8'
ENV LC_ALL='en_US.UTF-8'

ENV UPLOAD_FOLDER="/tmp/push-to-kindle"

ENV FLASK_APP=manager.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

EXPOSE 8001

COPY . .

ENV MG_API_KEY="secret"
ENV MG_EMAIL_TO_FOR_TEST="secret@kindle.cn"

ENV PRODUCTION_HOST="http://127.0.0.1:8001"

CMD [ "sh", "-c", "uwsgi uwsgi.ini" ]
