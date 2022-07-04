FROM python:3.9.13-slim-buster

RUN apt-get update

RUN apt-get install -y python-dev \
    libxml2-dev \
    libxslt1-dev \
    antiword \
    unrtf \
    poppler-utils \
    tesseract-ocr \
    flac \
    ffmpeg \
    lame \
    libmad0 \
    libsox-fmt-mp3 \
    sox \
    libjpeg-dev \
    swig \
    libpulse-dev

WORKDIR /app

RUN mkdir /files

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY __init__.py /app/

COPY exec.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/exec.sh

ENTRYPOINT [ "exec.sh" ]