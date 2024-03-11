import pika
import os

from dbHelper.mongoDB import update_status
from musicService.songWorker import SongWorker


class RabbitMQHandler:
    def __init__(self):
        self.channel = self.get_rabbit_connection()

    def get_rabbit_connection(self):
        url = os.environ.get('CLOUDAMQP_URL',
                             'amqps://sxquurom:B8tPjRwnTtlqCsHN8iOxr1ohqmiF0FJI@beaver.rmq.cloudamqp.com/sxquurom')
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        return channel

    def publish_on_queue(self, msg):
        self.channel.basic_publish(exchange='', routing_key='test', body=msg)
        self.channel.connection.close()

    def callback(self, ch, method, properties, body):
        print(f'getting {str(body)}')
        obj_name = body.decode('utf-8')
        try:
            song_worker = SongWorker(str(obj_name))
            song_worker.process_message()
        except Exception as e:
            update_status(obj_name, status="Failure")
            print(f'failed in the song progress for {obj_name} error: {e} ')

    def consume_on_queue(self):
        self.channel.basic_consume(queue='test', on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for messages:')
        self.channel.start_consuming()
        self.channel.connection.close()


def produce_on_rabbit(msg):
    rabbitmq_handler = RabbitMQHandler()
    rabbitmq_handler.publish_on_queue(msg)


def consume_rabbit():
    rabbitmq_handler = RabbitMQHandler()
    rabbitmq_handler.consume_on_queue()
