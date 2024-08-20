import pika
import requests
import os
# NOTE: This script will process jobs/messages.

def log_work(channel, method, properties, message):
    print(f'Job Received. {message}\n')

    url='https://mugwump303-flaskapp-a986c05f07c3.herokuapp.com/log_scheduler/'
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

# TODO: Add rabbitmq. Listen for messages and then do some job.
# rabbiturl = 'localhost'
# connection_parameters = pika.ConnectionParameters(rabbiturl)

rabbiturl = os.environ.get('CLOUDAMQP_URL', 'amqps://zhdyodgf:FCEzk5ncrYZxr7YcLwGqbz0AnQkFLELt@moose.rmq.cloudamqp.com/zhdyodgf')
# https://pika.readthedocs.io/en/stable/modules/parameters.html
connection_parameters = pika.URLParameters(rabbiturl)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='logschedule') # uses "default" exchange implicity

channel.basic_consume(queue='logschedule', auto_ack=True, on_message_callback=log_work)

print('Start Consuming')
channel.start_consuming()