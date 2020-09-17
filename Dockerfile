FROM python:3.7.9-slim-buster

COPY . /opt

RUN apt update -y && \
    apt install -y build-essential curl python3-dev && \
    apt install -y libffi-dev libssl-dev libevent-dev && \
    useradd pyuser -m -s /bin/bash && \
    mkdir /home/pyuser/app/ && \
    mkdir /home/pyuser/data/ && \
    mkdir /home/pyuser/secret/ && \
    mv /opt/* /home/pyuser/app && \
    cd /home/pyuser/app && \
    pip install -r requirements.txt && \
    chown -R pyuser:pyuser /home/pyuser

USER pyuser
WORKDIR /home/pyuser/app

EXPOSE 8888

ENTRYPOINT ["sh", "/home/pyuser/app/entrypoint.sh"]
