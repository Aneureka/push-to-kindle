FROM python:3.9
WORKDIR /app
RUN apt-get install gcc
COPY . .

RUN pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "sh", "-c", "uwsgi uwsgi.ini" ]
EXPOSE 8001
