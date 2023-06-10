import random
import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types

main_url = 'https://www.anekdot.ru/tags/'
API_KEY = '5897566066:AAEiGnyPej0XfaqNoDkyX2XsVu97To0rtCY'

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


bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Анекдот дня 😂'), types.KeyboardButton('Категории 📚'), types.KeyboardButton('Рандомный 🎲'))
    bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Анекдот дня 😂':
        bot.send_message(message.chat.id, 'МЕГА РЖОМБА')
    if message.text == 'Категории 📚':
        bot.send_message(message.chat.id, 'Выберите категорию:')
    if message.text == 'Рандомный 🎲':
        bot.send_message(message.chat.id, 'РАНДОМНАЯ РЖАКА')  


bot.polling()

