import telebot
import yfinance as yf
import time

bot_token = '1284597640:AAGFQYIftrSQrxhROzwmqD2ZK7pmmzBX8_4'

bot = telebot.TeleBot(token=bot_token)

def find_dollar(msg):
    for text in msg:
        if '$' in text:
            return text[1:]+".JK"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'To be defined')

@bot.message_handler(func=lambda msg: msg.text is not None and '$' in msg.text)
def at_answer(message):
    texts = message.text.split()
    stock_str = find_dollar(texts)
    stock = yf.Ticker(stock_str)

    bot.reply_to(message, stock.info)

bot.polling()
