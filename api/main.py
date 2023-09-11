from fastapi import FastAPI
import pika
#import logging
#import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='dummy-queue')

app = FastAPI()
#logger = logging.getLogger("gunicorn.error")
#logging.basicConfig(filename='app.log', level=logging.INFO)
#logger = logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


import routes

