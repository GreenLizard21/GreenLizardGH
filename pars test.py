import requests
from bs4 import BeautifulSoup
import telebot

url = 'https://uaf.ua/referee-committee/library/appointments'

bot = telebot.TeleBot("2029865910:AAFSUW2-KKX_SKld-yNWx3wDHAQXtF-HxVc")

page = requests.get(url)

new_news = []
news = []

soup = BeautifulSoup(page.text, "html.parser")

news = soup.findAll('a', class_='uk-link-reset')

for data in news:
    new_news.append(data.text)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, '\n'.join(new_news))

bot.polling( none_stop = True )