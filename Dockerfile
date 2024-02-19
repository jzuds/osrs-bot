FROM python:3.11-slim

RUN apt-get update \
  && apt-get -y install tesseract-ocr \
  && apt-get -y install ffmpeg libsm6 libxext6 \
  && apt-get -y install xvfb \
  && apt-get -y install python3-tk

ENTRYPOINT ["/bin/bash"]