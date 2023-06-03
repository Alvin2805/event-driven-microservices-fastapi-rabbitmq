import pika
import json
from model import User
from database import session
import time

time.sleep(100)

connection = pika.BlockingConnection(pika.URLParameters("amqp://alvin:Zhiffahmi3310@rabbitserver"))
channel = connection.channel()
channel.queue_declare(queue='service1')

def on_request(ch, method, props, body):
    get_msg = body

    print("I got the data is : %r " %get_msg)

    read_data = json.loads(get_msg)

    nik = read_data["username"]
    email_addr = read_data["email"]

    new_data = User()
    new_data.username = nik
    new_data.password = "Img" + nik
    new_data.email = email_addr
    session.add(new_data)
    session.commit()
    session.refresh(new_data)

    response = str(new_data.id)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='service1', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()