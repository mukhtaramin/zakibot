import telebot
import time

bot_token = '1284597640:AAGFQYIftrSQrxhROzwmqD2ZK7pmmzBX8_4'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')

bot.polling()