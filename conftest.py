import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture(scope='class')
def browser():
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(6)
    yield browser
    browser.quit()
