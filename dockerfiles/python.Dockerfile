FROM python:3.9-slim
RUN apt update && apt install -y jq
WORKDIR /home/app
