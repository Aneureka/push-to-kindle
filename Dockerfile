FROM python:latest

LABEL maintainer=Yinr<yinr@yinr.cc>

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV UPLOAD_FOLDER="/tmp/push-to-kindle"

ENV FLASK_APP=manager.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

EXPOSE 8001

CMD [ "sh", "-c", "uwsgi uwsgi-docker.ini" ]

COPY . .

# ENV MG_API_KEY
# ENV PRODUCTION_HOST
