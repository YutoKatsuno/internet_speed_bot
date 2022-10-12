from selenium import webdriver
from selenium.webdriver.common import service


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        chrome_service = service.Service(executable=driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.down: int = 0
        self.up: int = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass
