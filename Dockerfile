FROM ubuntu:latest

WORKDIR /app

RUN apt update && apt install -y python3 python3-dev python3-pip python3-venv unzip libsm6 libxext6 libgl1 libglib2.0-0
RUN python3 -m venv .venv

COPY . .

EXPOSE 3001
CMD [ "bash", "start.sh" ]
