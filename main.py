import telebot
from tok import TG_TOK
bot = telebot.TeleBot(TG_TOK)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,'Привет!')


bot.infinity_polling()
