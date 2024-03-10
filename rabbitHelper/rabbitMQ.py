import pika
import os


class RabbitMQHandler:
    def __init__(self):
        self.channel = self.get_rabbit_connection()
        self.response = None

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
        self.process_message(body)

    def consume_on_queue(self):
        self.channel.basic_consume(queue='test', on_message_callback=self.callback, auto_ack=True)
        # Close the connection
        self.channel.connection.close()


def produce_on_rabbit(msg):
    rabbitmq_handler = RabbitMQHandler()
    rabbitmq_handler.publish_on_queue(msg)


def consume_rabbit():
    rabbitmq_handler = RabbitMQHandler()
    rabbitmq_handler.consume_on_queue()
    return rabbitmq_handler.response


if __name__ == '__main__':
    produce_on_rabbit("ali")
    res = consume_rabbit()
    print(res)
