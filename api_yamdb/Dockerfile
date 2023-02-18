FROM python:3.7-slim

WORKDIR /app

COPY ./api_yamdb/requirements.txt .

RUN apt-get update -y \
&& apt-get upgrade -y pip \
&& pip install --upgrade pip \
&& pip install -r /app/requirements.txt --no-cache-dir

COPY . .

#CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]