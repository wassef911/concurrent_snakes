import asyncio
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


async def get_url_content(url: str, driver) -> Dict:
    driver.get(url)
    return driver.page_source, driver.title


async def main(urls: List[str]) -> None:
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    tasks = [asyncio.create_task(get_url_content(url, driver)) for url in urls]
    for task in tasks:
        await task
    driver.quit()
