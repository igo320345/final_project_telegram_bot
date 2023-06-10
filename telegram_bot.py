import random
import requests
from bs4 import BeautifulSoup as BS

main_url = 'https://www.anekdot.ru/tags/'

# функция получения анекдотов по данной ссылке
def parse_jokes(website_url):
    request = requests.get(website_url)
    soup = BS(request.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [i.text for i in jokes]

# функция формирования ссылку
def get_url():
    return main_url + input('Введите тему анекдота: ')

def get_joke_day():
    joke_day_url = 'https://www.anekdot.ru/release/anekdot/day/'
    return parse_jokes(joke_day_url)[0]

# вывод случайного анекдота по теме
mass = parse_jokes(get_url())
print(mass[random.randint(0, len(mass))])

# вывод анекдота дня
print(get_joke_day())


