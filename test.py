
import telebot

bot = telebot.TeleBot("2029865910:AAFSUW2-KKX_SKld-yNWx3wDHAQXtF-HxVc")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, '123')

bot.polling( none_stop = True )
