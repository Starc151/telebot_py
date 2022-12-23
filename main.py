import telebot
from telebot import types
from game import *
from tok import TG_TOK

bot = telebot.TeleBot(TG_TOK)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,'Давайте поиграем!')
    print_buttom(message)

def print_buttom(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(view_xo(1))
    item2 = types.KeyboardButton(view_xo(2))
    item3 = types.KeyboardButton(view_xo(3))
    item4 = types.KeyboardButton(view_xo(4))
    item5 = types.KeyboardButton(view_xo(5))
    item6 = types.KeyboardButton(view_xo(6))
    item7 = types.KeyboardButton(view_xo(7))
    item8 = types.KeyboardButton(view_xo(8))
    item9 = types.KeyboardButton(view_xo(9))

    markup.add(item1, item2, item3)
    markup.add(item4, item5, item6)
    markup.add(item7, item8, item9)
    bot.send_message(message.chat.id,'Ваш ход',reply_markup=markup)

@bot.message_handler(content_types='text')
def move(message):
    human_move(message.text)
    if victory('x') != 'empty':
        bot.send_message(message.chat.id, victory('x'))
        stop_game(message)
        return
    comp_move()
    if victory('o') != 'empty':
        bot.send_message(message.chat.id, victory('o'))
        stop_game(message)
    print_buttom(message)

@bot.message_handler(commands=['stop'])
def stop_game(message):
    bot.send_message(message.chat.id, "Игра остановлена!")
    set_global()
    start_game(message)

bot.infinity_polling()