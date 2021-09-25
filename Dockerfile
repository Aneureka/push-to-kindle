FROM python:3.7
WORKDIR /app
RUN apt-get install gcc
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "sh", "-c", "uwsgi uwsgi.ini" ]
EXPOSE 8001
