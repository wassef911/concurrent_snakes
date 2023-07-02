from os import path
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from .utils import OUTPUT_FOLDER, slugify, timestamp, write_dict_to_file


async def get_url_content(url: str, driver) -> Dict:
    driver.get(url)
    return driver.page_source, driver.title


async def main(urls: List[str]) -> None:
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    for url in urls:
        result, title = await get_url_content(url, driver)
        out_path = path.join(OUTPUT_FOLDER, f"{slugify(title)}_{timestamp()}.txt")
        try:
            write_dict_to_file(result, out_path)
        except FileNotFoundError:
            print(f"check that {out_path} exists!")
    driver.quit()
