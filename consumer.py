import json

import pika

params = pika.URLParameters('amqps://chzdnyno:cxtMA_neMNuK_uWNSPOq7j9daGGiG00h@gull.rmq.cloudamqp.com/chzdnyno')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='aula')

def callback(ch, method, properties, body):
    print('Received in auladocker')
    data = json.loads(body)
    print(data)

channel.basic_consume(queue='aula', on_message_callback=callback,
                      auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()