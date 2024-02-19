FROM python:3.11-slim

WORKDIR /osrs-bot

COPY . /osrs-bot

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/bin/bash"]