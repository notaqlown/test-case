FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install -r requirements.txt

COPY wait-for-it.sh /app/wait-for-it.sh

RUN chmod +x /app/wait-for-it.sh

COPY . .

CMD ["./wait-for-it.sh", "rabbitmq", "5672", "--", "python", "main.py"]