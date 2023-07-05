import asyncio
import socket
import sys
import time
from typing import Dict, List

import aiohttp
from aiokafka import AIOKafkaProducer
from decouple import config

from .src.utils import URLS

TOPIC = config("KAFKA_TOPIC")
producer = AIOKafkaProducer(bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVER"))


async def fetch_url(url: str) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main(URLS: List[str]) -> None:
    while True:
        start_time = time.time()
        for url in URLS:
            data = await fetch_url(url)
            try:
                future = await producer.send(TOPIC, data)
            except Exception as e:
                print(e)
                raise e
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"looped through all urls in {exec_time}")


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(URLS))
    except Exception as e:
        sys.exit(1)
    finally:
        loop.close()
