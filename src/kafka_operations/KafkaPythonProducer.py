import time
import threading
from kafka import KafkaProducer
from connexion import request

def produce():
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', max_request_size=10000000)
    print("create producer")

    req = request.get_json()
    msg = req["message"]
    topic_name = req["topic"]

    producer.send(topic_name, msg.encode('utf-8'))
    producer.close()

    return 'OK'

