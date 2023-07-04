from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_url_content(url: str, driver) -> Dict:
    driver.get(url)
    return driver.page_source, driver.title


def main(urls: List[str]) -> None:
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    for url in urls:
        get_url_content(url, driver)
    driver.quit()
