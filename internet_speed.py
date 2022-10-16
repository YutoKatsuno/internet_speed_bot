from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        driver_path = "/Users/katsunoyuutou/Development/chromedriver"
        chrome_service = service.Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Start speed test
        time.sleep(5)
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()

        # Get the result
        time.sleep(120)
        data_list = self.driver.find_elements(By.CSS_SELECTOR, 'div.result-data.u-align-left span')
        try:
            self.down = data_list[0].text
        except IndexError:
            self.down = "計測できませんでした"
        try:
            self.up = data_list[1].text
        except IndexError:
            self.up = "計測できませんでした。"

    def tweet_at_provider(self, email, password, username):
        self.driver.get("https://twitter.com/")

        # Login
        time.sleep(3)
        login_button = self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n.r-2o02ov a")
        login_button.click()
        time.sleep(3)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 input")
        input_email.send_keys(email, Keys.ENTER)
        time.sleep(3)
        user_name = self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 input")
        user_name.send_keys(username, Keys.ENTER)
        time.sleep(3)
        input_password = self.driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n.r-mk0yit.r-13qz1uu input")
        input_password.send_keys(password, Keys.ENTER)

        # Tweet
        time.sleep(3)
        message = self.driver.find_element(By.CSS_SELECTOR, 'div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        message.click()
        message.send_keys(f'download: {self.down} upload: {self.up}')
        submit = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        submit.click()
