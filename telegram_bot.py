import telebot
from telebot import types

API_KEY = '5897566066:AAEiGnyPej0XfaqNoDkyX2XsVu97To0rtCY'

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