import pika
import uuid
import json

class SendEventMsg(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="host.docker.internal"))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="",exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None
        self.corr_id = None

    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,msg,queue_channel):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key=queue_channel,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=json.dumps(msg)
        )
        self.connection.process_data_events(time_limit=None)
        return self.response