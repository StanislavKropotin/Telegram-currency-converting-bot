import telebot
from Config import *
from extensions import Converter, APIException
bot = telebot.TeleBot(TOKKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Здравствуйте!\nЧтобы узнать курс интересующей Вас валюты, спросите бота в следующем формате:\nНаименование валюты\
\nВ какую валюту хотите переводить\nКоличество переводимой валюты\nПример корректного ввода:\nЙена(Япония) Доллар(Австралия) 2000\
\nЧтобы увидеть список всех доступных валют введите команду:/values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    parameters = message.text.split()
    try:
        if len(parameters) != 3:
            raise APIException("Нужно ввести три параметра!")
        answer = Converter.get_price(*parameters)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}" )
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}" )
    else:
        bot.reply_to(message,answer)


bot.polling(none_stop=True)



