FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install -r requirements.txt

COPY wait-for-it.sh /app/wait-for-it.sh

COPY . .
RUN chmod +x /app/wait-for-it.sh
CMD ["./wait-for-it.sh", "rabbitmq", "5672", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
