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

@bot.message_handler(commands=['change'])
def change(m):
    bot.send_message(m.chat.id, 'Ведите кодировку нужной валюты')
    view_button_bot(m)
    bot.register_next_step_handler(m, select_currency_bot)
    bot.send_message(m.chat.id, dict_valutes(), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

def select_currency_bot(m):
    bot.send_message(m.chat.id, select_currency(m))

# @bot.message_handler(content_types=['text'])
def view_button_bot(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кодировки валют")
    markup.add(item1)
    bot.send_message(m.chat.id,'Список можно посмотреть по кноппе ниже', reply_markup=markup)
    # if m.text == "Кодировки валют":
        # bot.send_message(m.chat.id, dict_valutes(), reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')

    

bot.infinity_polling()
