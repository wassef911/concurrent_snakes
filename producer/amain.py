import asyncio
import sys
import time
from typing import Dict, List

import aiohttp
from aiokafka import AIOKafkaProducer
from decouple import config
from src.utils import URLS

TOPIC = config("KAFKA_TOPIC", default="async_data")


async def fetch_url(url: str) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def process_url(url: str, producer: AIOKafkaProducer, topic: str):
    data = await fetch_url(url)
    await producer.send(topic, f"{data}".encode())


async def main(URLS: List[str]) -> None:
    producer = AIOKafkaProducer(
        bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVER", default="localhost:9093")
    )
    await producer.start()
    while True:
        start_time = time.time()
        tasks = [process_url(url, producer, TOPIC) for url in URLS]
        await asyncio.gather(*tasks)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"looped through all urls in {exec_time}")


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(URLS))
    except Exception as e:
        print(e)
        sys.exit(1)
