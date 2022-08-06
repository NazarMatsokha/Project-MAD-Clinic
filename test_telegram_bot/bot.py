import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Раді вас вітати, <b>{message.from_user.first_name}</b>, я "Гей-детектор бот" який був створений для того щоб виявляти вашу сексальну орієнтацію!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    sti = open('static/angry_nigga.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)






@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ну скажіть натурал би став посилати таке фото?')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Інформація", url="https://pornhub.com"))
    bot.send_message(message.chat.id, 'Перейди на сайт', reply_markup=markup)


bot.polling(none_stop=True)