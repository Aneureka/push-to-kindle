FROM python:3.7-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "sh", "-c", "uwsgi uwsgi.ini" ]
EXPOSE 8001