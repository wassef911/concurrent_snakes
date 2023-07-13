import asyncio
import sys

import aiohttp
from aiokafka import AIOKafkaConsumer
from decouple import config

TOPIC = config("KAFKA_TOPIC", default="async_data")


async def main() -> None:
    consumer = AIOKafkaConsumer(
        TOPIC, bootstrap_servers=config("KAFKA_BOOTSTRAP_SERVER"), group_id="amain"
    )
    await consumer.start()
    while True:
        async for msg in consumer:
            print("Received: {}".format(msg.value.decode("utf-8")))


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print(e)
        sys.exit(1)
