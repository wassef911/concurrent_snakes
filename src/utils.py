import re
import time
from datetime import datetime
from typing import Dict, List

import unidecode

OUTPUT_FOLDER = "/home/wassef/Desktop/code/personal/async_python/src/out"
URLS = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(40)]

timestamp = lambda: datetime.timestamp(datetime.now())


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r"[\W_]+", "-", text)


def write_dict_to_file(data, file_path):
    with open(file_path, mode="w") as file:
        file.write(str(data))
