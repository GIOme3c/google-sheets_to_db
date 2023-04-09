FROM python:alpine

WORKDIR /app

COPY . /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]