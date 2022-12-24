import telebot
from change import select_currency
from tok import TG_TOK
bot = telebot.TeleBot(TG_TOK)
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,'Привет!')

@bot.message_handler(commands=['game'])
def game_bot(message):
    bot.send_message(message.chat.id,'Игра пока отключена')

@bot.message_handler(commands=['change'])
def change(message):
    bot.send_message(message.chat.id,'Укажите кодировку нужной валюты')
    bot.send_message(message.chat.id,'Список можно посмотреть по кноппе ниже')
    bot.send_message(message.chat.id,'Curhelp')
    res = bot.register_next_step_handler(message, select_currency_bot)

def select_currency_bot(message):
    bot.send_message(message.chat.id, select_currency(message))

bot.infinity_polling()
