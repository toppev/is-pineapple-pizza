FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y curl

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu

ADD . /app

# Number of workers for easy scaling, ~doubles memory usage
ARG WEB_CONCURRENCY=1
ENV WEB_CONCURRENCY=${WEB_CONCURRENCY}

WORKDIR /app/server

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "60", "--access-logfile", "-", "app:app"]