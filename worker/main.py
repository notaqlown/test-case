import pika
import json
import requests
import logging
from database import Session, Request
import time
import sys


logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


def post_req(data):
    request = requests.post(url='http://dummy_service:8001/calculate/', json=data)
    return request.json()

def callback(ch, method, properties, body):
    analyzed_text = analyze_text(body)
    new_data = post_req(analyzed_text)

    session = Session()
    session.add(Request(
        id=new_data['req_id'],
        cadastre=new_data['cadastre'],
        latitude=new_data['lat'],
        longitude=new_data['lon'],
        calc=new_data['calc']
    ))
    session.commit()

    logging.info(f' new {new_data}')

    ch.basic_ack(delivery_tag=method.delivery_tag)


def analyze_text(text):

    time.sleep(10)
    data = json.loads(text)
    json_text = {
                "req_id":str(data["req_id"]),
                "cadastre":str(data["cadastre"]),
                "lat":float(data["lat"]),
                "lon":float(data["lon"])
            }

    return json_text


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='dummy-queue')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='dummy-queue', on_message_callback=callback)
channel.start_consuming()
