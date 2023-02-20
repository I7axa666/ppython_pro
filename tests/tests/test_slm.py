from selenium import webdriver
import time
from settings import ya_login, ya_password
from selenium.webdriver.common.by import By
import unittest as ut


class TestYaPass(ut.TestCase):
    url = "https://passport.yandex.ru/auth/"
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    )
    driver = webdriver.Chrome(executable_path="tests/chromedriver.exe", options=options)

    def test_auth(self):
        try:
            self.driver.get(url=self.url)
            time.sleep(1)

            email_input = self.driver.find_element("id", "passp-field-login")
            email_input.clear()
            email_input.send_keys(ya_login)
            time.sleep(1)

            login_button = self.driver.find_element("id", "passp:sign-in").click()
            time.sleep(1)

            password_input = self.driver.find_element("id", "passp-field-passwd")
            password_input.clear()
            password_input.send_keys(ya_password)
            time.sleep(1)

            password_button = self.driver.find_element("id", "passp:sign-in").click()
            time.sleep(3)

            data_button = self.driver.find_element(
                By.CLASS_NAME, "Card_label__AG2MY"
            ).text

        except Exception as ex:
            print(ex)
        finally:
            self.assertEqual(data_button, "Обо мне")
            self.driver.close()
            self.driver.quit()