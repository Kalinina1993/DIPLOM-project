from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


class TestLoginNewUser:
    def test_new_user_exist(self, init_driver):
        """Checking that new user_2 is created"""
        driver = init_driver
        driver.get("http://localhost:8000/admin/lo")
        username = driver.find_element(By.NAME, "username")
        username.send_keys("admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("password")
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get("http://localhost:8000/admin/auth/user/")
        element = driver.find_element(By.CSS_SELECTOR, "#changelist-form > p")
        assert element.text == "3 users", f"Error"

    def test_new_user_login(self, init_driver):
        """Testing login with new user_2"""
        driver = init_driver
        # driver.get("http://localhost:8000/admin/lo")
        driver.find_element(By.CSS_SELECTOR, "#user-tools > a:nth-child(4)").click()
        driver.find_element(By.CSS_SELECTOR, "#content > p:nth-child(3) > a").click()
        username = driver.find_element(By.NAME, "username")
        username.send_keys("user_2")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("*VpH6-HG.cay3fE")
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get("http://localhost:8000/admin/")
        element = driver.find_element(By.CSS_SELECTOR, "#content > h1")
        assert element.text == "Site administration", f"Error"


class TestDeleteImage:
    def test_post_page_title(self, init_driver):
        """Testing correct title of post page"""
        driver = init_driver
        driver.get("http://localhost:8000/admin/lo")
        username = driver.find_element(By.NAME, "username")
        username.send_keys("admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("password")
        driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get("http://localhost:8000/admin/app/post/")
        title = driver.title
        assert title == "Select post to change | Django site admin", f"Error"

    def test_delete_image(self, init_driver):
        """Delete the first post"""
        driver = init_driver
        # driver.get("http://localhost:8000/admin/lo")
        # username = driver.find_element(By.NAME, "username")
        # username.send_keys("admin")
        # password = driver.find_element(By.NAME, "password")
        # password.send_keys("password")
        # driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").click()
        driver.get("http://localhost:8000/admin/app/post/")
        driver.find_element(By.NAME, "_selected_action").click()
        action = driver.find_element(By.NAME, "action")
        action.send_keys("D")
        driver.find_elements(By.CSS_SELECTOR, "#changelist-form > div.actions > label > select > option:nth-child(2)")
        driver.find_element(By.CLASS_NAME, "button").click()
        driver.find_element(By.CSS_SELECTOR, "#content > form > div > input[type=submit]:nth-child(4)").click()
        driver.get("http://localhost:8000/admin/app/post/")
        element = driver.find_element(By.CLASS_NAME, "paginator")
        assert element.text == "0 posts", f"Error"





