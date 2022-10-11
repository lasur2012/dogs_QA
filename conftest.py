from loguru import logger

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def get_options():
    options = Options()
    options.headless = True
    return options


@pytest.fixture()
def browser():
    logger.info("--- Starting browser ---")
    options = get_options()
    browser = webdriver.Chrome(options=options)
    yield browser
    logger.info("--- Quitting browser ---")
    browser.quit()

