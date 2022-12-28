from telebot import types
import telebot
from change import *
from tok import TG_TOK
bot = telebot.TeleBot(TG_TOK)

@bot.message_handler(commands=['start'])
def start_bot(m):
    bot.send_message(m.chat.id, 'Привет!')

@bot.message_handler(commands=['game'])
def game_bot(m):
    bot.send_message(m.chat.id, 'Игра пока отключена')

@bot.message_handler(commands=['change'], content_types='text')
def change(m):
    bot.send_message(m.chat.id, 'Ведите кодировку нужной валюты')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Кодировки валют")
    markup.add(item)
    bot.send_message(m.chat.id, 'Список можно посмотреть по кнопке ниже', reply_markup=markup)
    bot.register_next_step_handler(m, select_currency_bot)

def select_currency_bot(m):
    if m.text == "Кодировки валют":
        bot.send_message(m.chat.id, valutes(),
                        reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(m, select_currency_bot)
    else:
        bot.send_message(m.chat.id, currency_exchange(m),
                                    reply_markup=types.ReplyKeyboardRemove())

bot.infinity_polling()
