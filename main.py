import os
from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(EMAIL, PASSWORD, USERNAME)

print(f'download: {bot.down}')
print(f'upload: {bot.up}')

