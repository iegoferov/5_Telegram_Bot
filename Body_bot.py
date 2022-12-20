from extensions import Read_Token, Get_Price, Bot_Exception
import telebot



bot_value = ['доллар', 'евро', 'рубль']
usd_value = ['доллар', 'долларов', 'долларах']
rub_value = ['рубль', 'рублей', 'рублях']
TOKEN = Read_Token.read_token()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_start_help(message):
    bot.send_message(message.chat.id, f'Бот возвращает цену на определённое количество валюты (евро, доллар или рубль). Человек должен отправить сообщение боту со следующей информацией через пробел:\n 1) Имя валюты, цену которой он хочет узнать\n 2) Имя валюты, в которой надо узнать цену первой валюты\n 3) Количество первой валюты через пробел\n Например, евро рубль 5462')
    bot.send_message(message.chat.id, 'Список доступных команд:\n/start\n/help\n/values')

@bot.message_handler(commands=['values'])
def send_values(message):
    bot.send_message(message.chat.id,'Доступные валюты:\nЕвро\nДоллар\nРубль')

@bot.message_handler(commands=['values'])
def send_values(message):
    bot.send_message(message.chat.id,'Доступные валюты:\nЕвро\nДоллар\nРубль')

@bot.message_handler(content_types=['text'])
def get_rate(message):
    value = message.text.split(' ')
    try:
        if len(value) != 3:
            raise Bot_Exception (f'Введено некоректное число параметров, равное {len(value)}, выполните команду /help')
        base, quote, amount = value[0].lower(), value[1].lower(), value[2]
        if base not in bot_value:
            raise Bot_Exception(f'Название валюты: {base.upper()} введено некорректно, выполните команду /help')
        elif quote not in bot_value:
            raise Bot_Exception(f'Название валюты: {quote.upper()} введено некорректно, выполните команду /help')
        elif not amount.isdigit():
            raise Bot_Exception(f'Количество валюты: {amount.upper()} введено некорректно, выполните команду /help')
        price = Get_Price.get_price(base, quote, amount)

    except Bot_Exception as e:
        bot.reply_to(message, f'Ошибка ввода {e}')

    except Exception as e:
        bot.reply_to(message, f'Произошла непредвиденая ошибка {e}')

    else:
        if quote == usd_value[0]:
            quote = usd_value[1]
        if quote == rub_value[0]:
            quote = rub_value[1]
        if base == usd_value[0]:
            base = usd_value[2]
        if base == rub_value[0]:
            base = rub_value[2]

        bot.send_message(message.chat.id, f'Число {quote.upper()} в {base.upper()} = {price}')

bot.polling(none_stop=True)





