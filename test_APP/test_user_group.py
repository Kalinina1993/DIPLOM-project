from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from config import Datas

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


class TestLogin:
    def test_username_link_is_visible(self, init_driver, url_lo):
        """Testing username link for visible"""
        driver = init_driver
        driver.get(url_lo)
        flag = driver.find_element(By.NAME, "username")
        assert flag.is_enabled()

    def test_password_link_is_visible(self, init_driver, url_lo):
        """Testing password link for visible"""
        driver = init_driver
        driver.get(url_lo)
        flag = driver.find_element(By.NAME, "password")
        assert flag.is_enabled(), f"Error: Link is not visible"

    def test_login_page_title(self, init_driver, url_lo):
        """Testing correct title of login page"""
        driver = init_driver
        driver.get(url_lo)
        title = driver.title
        assert title == "Log in | Django site admin", f"Error:Incorrect title "

    def test_login(self, init_driver, url_lo, url_adm):
        """Checking the location of window administration"""
        driver = init_driver
        driver.get(url_lo)
        username = driver.find_element(By.NAME, "username")
        username.send_keys(Datas.username)
        password = driver.find_element(By.NAME, "password")
        password.send_keys(Datas.password)
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get(url_adm)
        element = driver.find_element(By.CSS_SELECTOR, "#content > h1")
        assert element.text == "Site administration", f"Error: Not administration page"

    def test_group_exist(self, init_driver, url_adm):
        """Checking that creating group_1 is existed"""
        driver = init_driver
        driver.get(url_adm)
        driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > "
                                             "th > a").click()
        element = driver.find_element(By.CLASS_NAME, "paginator")
        assert element.text == "1 group", f"Error: 0 group"


class TestAdmin:
    def test_group_page(self, init_driver, url_lo, url_adm):
        """Checking of location window of groups """
        driver = init_driver
        driver.get(url_lo)
        username = driver.find_element(By.NAME, "username")
        username.send_keys("admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("password")
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get(url_adm)
        driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > "
                                             "th > a").click()
        element = driver.find_element(By.CSS_SELECTOR, "#content > h1")
        assert element.text == "Select group to change", f"Error: Not group page"

    def test_group_page_title(self, init_driver, url_group):
        """Testing correct group title"""
        driver = init_driver
        driver.get(url_group)
        title = driver.title
        assert title == "Select group to change | Django site admin", f"Error: incorrect title"

    def test_group_search_link_is_visible(self, init_driver, url_group):
        """Testing that group search link is visible"""
        driver = init_driver
        driver.get(url_group)
        flag = driver.find_element(By.ID, "searchbar")
        assert flag.is_enabled(), f"Error: Link is not visible"

    def test_user_page_title(self, init_driver, url_user):
        """Testing correct title of user page"""
        driver = init_driver
        driver.get(url_user)
        title = driver.title
        assert title == "Select user to change | Django site admin", f"Error: Incorrect title"

    def test_user_search_is_visible(self, init_driver, url_user):
        """Testing that user search link is visible"""
        driver = init_driver
        driver.get(url_user)
        flag = driver.find_element(By.NAME, "q")
        assert flag.is_enabled(), f"Error:Link is not visible "


class TestCheck:
    def test_adding_user_in_group(self, init_driver, url_lo, url_user):
        """Checking that creating user_1 added in group_1"""
        driver = init_driver
        driver.get(url_lo)
        username = driver.find_element(By.NAME, "username")
        username.send_keys(Datas.username)
        password = driver.find_element(By.NAME, "password")
        password.send_keys(Datas.password)
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get(url_user)
        driver.find_element(By.CSS_SELECTOR, "#result_list > tbody > tr:nth-child(2) > th > a").click()
        element = driver.find_element(By.CSS_SELECTOR, "#id_groups_to > option")
        print(f"user_1 added in", element.text)
        assert element
