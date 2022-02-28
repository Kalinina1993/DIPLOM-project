import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="class")
def url_adm():
    url = "http://localhost:8000/admin"
    return url


@pytest.fixture(scope="class")
def url_lo():
    url = "http://localhost:8000/admin/lo"
    return url


@pytest.fixture(scope="class")
def url_group():
    url = "http://localhost:8000/admin/auth/group/"
    return url


@pytest.fixture(scope="class")
def url_user():
    url = "http://localhost:8000/admin/auth/user/"
    return url


@pytest.fixture(scope="class")
def url_post():
    url = "http://localhost:8000/admin/app/post/"
    return url   
