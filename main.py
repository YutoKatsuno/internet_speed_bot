import os
from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

download = bot.down
upload = bot.up
print(f'down: {download}')
print(f'up: {upload}')
