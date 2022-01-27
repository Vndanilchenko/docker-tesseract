# base image
FROM tiangolo/meinheld-gunicorn-flask

# update packages
RUN apt-get update
RUN apt-get install tesseract-ocr-rus -y

# copy files
COPY requirements.txt requirements.txt
COPY documents documents
COPY main.py main.py

# install requirements
RUN python3 -m pip install -r requirements.txt
