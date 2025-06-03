FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:5000"]

EXPOSE 5000