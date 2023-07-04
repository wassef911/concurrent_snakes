#!/usr/bin/env python

import asyncio
import time

from src.asynchronous import main as amain
from src.synchronous import main
from src.utils import URLS

start_time = time.time()
main(URLS)
end_time = time.time()
sync_exec_time = end_time - start_time
print(f"Execution time sync: {sync_exec_time} seconds")


start_time = time.time()
asyncio.run(amain(URLS))
end_time = time.time()
async_exec_time = end_time - start_time
print(f"Execution time async: {async_exec_time} seconds")

print(f"async is faster by: {sync_exec_time - async_exec_time } seconds")
