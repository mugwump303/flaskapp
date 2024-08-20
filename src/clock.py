from apscheduler.schedulers.blocking import BlockingScheduler
import pika
import datetime
import os

# NOTE: This script handles scheduling/queuing jobs.

# rabbiturl = 'localhost'
# connection_parameters = pika.ConnectionParameters(rabbiturl)

rabbiturl = os.environ.get('CLOUDAMQP_URL', 'amqps://zhdyodgf:FCEzk5ncrYZxr7YcLwGqbz0AnQkFLELt@moose.rmq.cloudamqp.com/zhdyodgf')

# https://pika.readthedocs.io/en/stable/modules/parameters.html
connection_parameters = pika.URLParameters(rabbiturl)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='logschedule') # uses "default" exchange implicity

sched = BlockingScheduler()

i=0
# @sched.scheduled_job('interval', seconds=10)
@sched.scheduled_job('interval', minutes=30)
def timed_job():
    global i
    now = datetime.datetime.now()
    message = f"Job {i} Given: {now}"
    i += 1

    # publishes a message to default exchange to the "logschedule" queue.
    channel.basic_publish(exchange='', routing_key='logschedule', body=message)

    print('This job is run every ten seconds.')

print('Start Clock')
sched.start()
