from selenium import webdriver
import asyncio
from typing import List, Dict

FIREFOX_DRIVER_PATH = "/usr/bin/firefox"


async def get_url_content(url: str, driver) -> Dict:
    await driver.get(url)
    return driver.page_source


async def main(urls: List[str]) -> None:
    driver = webdriver.Firefox(FIREFOX_DRIVER_PATH)
    for i in urls:
        result = await get_url_content(i, driver)
        print(result)
    driver.quit()


asyncio.run(main(["https://www.scrapethissite.com/pages/simple/"]))
