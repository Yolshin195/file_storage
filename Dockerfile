FROM python:3.12.1

RUN mkdir "/file_storage"

WORKDIR /file_storage

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
