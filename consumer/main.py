import socket
import sys

from confluent_kafka import Consumer
from decouple import config

TOPIC = config("KAFKA_TOPIC")
conf = {
    "bootstrap.servers": config("KAFKA_BOOTSTRAP_SERVER"),
    "group.id": socket.gethostname(),
}
consumer = Consumer(conf)


def main() -> None:
    consumer.subscribe([TOPIC])
    while True:
        msg = consumer.poll(1.0)
        if msg.error():
            raise Exception(msg.error() if msg != None else "faced some error")
        print("Received: {}".format(msg.value().decode("utf-8")))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)
