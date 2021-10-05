import requests
from bs4 import BeautifulSoup

url = 'https://uaf.ua/referee-committee/library/appointments'

page = requests.get(url)

new_news = []
news = []

soup = BeautifulSoup(page.text, "html.parser")

news = soup.findAll('a', class_='uk-link-reset')

for data in news:
    new_news.append(data.text)

print('\n'.join(new_news))




