FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ../../new_test/worker/wait-for-it.sh /app/wait-for-it.sh

RUN chmod +x /app/wait-for-it.sh

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd

CMD ["./wait-for-it.sh", "rabbitmq", "5672", "--", "python", "main.py"]