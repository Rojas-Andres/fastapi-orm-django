FROM python:3.9.10

ENV PYTHONUNBUFFERED 1
COPY run.sh /usr/local/bin/run.sh
COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

RUN chmod 777 run.sh

EXPOSE 8000

ENTRYPOINT ["run.sh"]