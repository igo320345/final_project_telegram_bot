import random
import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types
from topics_file import topics

main_url = 'https://www.anekdot.ru/tags/'
API_KEY = '5897566066:AAEiGnyPej0XfaqNoDkyX2XsVu97To0rtCY'

bot = telebot.TeleBot(API_KEY)

# функция формирования ссылку
def get_url():
    return main_url + input('Введите тему анекдота: ')


# функция получения анекдотов по данной ссылке
def parse_jokes(website_url):
    request = requests.get(website_url)
    soup = BS(request.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [i.text for i in jokes]


# функция получения случайного анекдота дня
def get_joke_day():
    joke_day_url = 'https://www.anekdot.ru/release/anekdot/day/'
    day_jokes = parse_jokes(joke_day_url)
    return day_jokes[random.randint(0, len(day_jokes) - 1)]


# получение случайного анекдота из случайной темы
def get_random():
    random_joke = parse_jokes(main_url + topics[random.randint(0, len(topics) - 1)])
    return random_joke[random.randint(0, len(random_joke) - 1)]

# получение случайной шутки по теме
def get_topic_joke(joke_topic):
    topic_joke_url = main_url + joke_topic
    topic_joke = parse_jokes(topic_joke_url)
    return topic_joke[random.randint(0, len(topic_joke) - 1)]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Анекдот дня 😂'), types.KeyboardButton('Категории 📚'), types.KeyboardButton('Рандомный 🎲'))
    bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Анекдот дня 😂':
        bot.send_message(message.chat.id, get_joke_day())
    if message.text == 'Категории 📚':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), 
                   types.KeyboardButton('Вовочка 🤷‍♂'), 
                   types.KeyboardButton('Студенты 🤓'), 
                   types.KeyboardButton('Британские ученые 🧑‍🔬'),
                   types.KeyboardButton('Цитаты 💬'),
                   types.KeyboardButton('Программисты 🧑‍💻'), 
                   types.KeyboardButton('Вернуться в меню 🔙'))
        bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)
    if message.text == 'Рандомный 🎲':
        bot.send_message(message.chat.id, get_random())  
    
    if message.text == 'Вернуться в меню 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Анекдот дня 😂'), types.KeyboardButton('Категории 📚'), types.KeyboardButton('Рандомный 🎲'))
        bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup)
    
    if message.text == 'Студенты 🤓':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Студенты 🤓'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('студент'), reply_markup=markup)
        

    if message.text == 'Спорт 💪':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('спорт'), reply_markup=markup)
    
    if message.text == 'Вовочка 🤷‍♂':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Вовочка 🤷‍♂'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('вовочка'), reply_markup=markup)
    
    if message.text == 'Британские ученые 🧑‍🔬':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Британские ученые 🧑‍🔬'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('британские%20ученые'), reply_markup=markup)
    
    if message.text == 'Цитаты 💬':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Цитаты 💬'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('цитаты'), reply_markup=markup)
    
    if message.text == 'Программисты 🧑‍💻':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Программисты 🧑‍💻'), types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, get_topic_joke('программист'), reply_markup=markup)
    
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Спорт 💪'), 
                   types.KeyboardButton('Вовочка 🤷‍♂'), 
                   types.KeyboardButton('Студенты 🤓'), 
                   types.KeyboardButton('Британские ученые 🧑‍🔬'),
                   types.KeyboardButton('Цитаты 💬'),
                   types.KeyboardButton('Программисты 🧑‍💻'), 
                   types.KeyboardButton('Вернуться в меню 🔙'))
        bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

bot.polling()