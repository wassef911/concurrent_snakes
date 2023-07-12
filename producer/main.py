import socket
import sys
import time
from typing import Dict, List

import requests
from confluent_kafka import Producer
from decouple import config
from src.utils import URLS

TOPIC = config("KAFKA_TOPIC")
conf = {
    "bootstrap.servers": config("KAFKA_BOOTSTRAP_SERVER"),
    "client.id": socket.gethostname(),
}
producer = Producer(conf)


def fetch_url(url: str) -> Dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main(URLS: List[str]) -> None:
    while True:
        start_time = time.time()
        for url in URLS:
            data = fetch_url(url)
            producer.produce(TOPIC, f"{data}")
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"looped through all urls in {exec_time}")


if __name__ == "__main__":
    try:
        main(URLS)
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        producer.flush()
