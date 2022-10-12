from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        chrome_service = service.Service(executable=driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.down: float = 0
        self.up: float = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()

        time.sleep(60)
        data_list = self.driver.find_elements(By.CSS_SELECTOR, 'div.result-data.u-align-left span')
        self.down = data_list[0].text
        self.up = data_list[1].text

    def tweet_at_provider(self):
        pass
