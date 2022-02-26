import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome("/home/natasha/PycharmProjects/DIPLOM/chromedriver", )
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()

