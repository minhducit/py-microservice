=========================
Python Kafka Microservice
=========================

Service to allow to produce and consume message to/from Kafka stream  

Introduction
=============

This is docker-based open-api service that allows to produce the message to Kafka stream (via Python KafkaConsumer), and retrieve message (via Python KafkaProducer) 


Docker images:
=============
zookeeper:  ZooKeeper is used to manage the Kafka cluster. ZooKeeper is used to coordinate the brokers/cluster topology.
kafka: Kafka engine
py-service: Python service that communicate with Kafka: 
            - Produce message to Kafka via endpoint (i.e.,  /kafka-lib/produce)
			- Consume message by subscribe to certain Kafka topic


Build and test locally:
=======================

1. Build and start the service
docker-compose build --no-cache py-service
docker-compose up

2. Test
Endpoint: http://localhost:3044/kafka-lib/produce
Example body data (Json): 
{
    "message": "Here we go Kafka"
}



