from extensions import Read_Token, Get_Price, Bot_Exception
import telebot


true_value = ['доллар', 'евро', 'рубль']
try:
    true_value = ['доллар', 'евро', 'рубль']
    TOKEN = Read_Token.read_token()
    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler()
    def send_start(message):
        bot.send_message(message.chat.id, 'werwefsdfsdfgsgsdg')

    @bot.message_handler(commands=['start', 'help'])
    def send_start_help(message):
        bot.send_message(message.chat.id, f'Бот возвращает цену на определённое количество валюты (евро, доллар или рубль). Человек должен отправить сообщение боту со следующей информацией через пробел:\n 1) Имя валюты, цену которой он хочет узнать\n 2) Имя валюты, в которой надо узнать цену первой валюты\n 3) Количество первой валюты через пробел\n Например, евро рубль 5462')

    @bot.message_handler(commands=['values'])
    def send_values(message):
        bot.send_message(message.chat.id,'Доступные валюты:\nЕвро\nДоллар\nРубль')

    @bot.message_handler(content_types=['text'])
    def get_rate(message):
        value = message.text.split(' ')
        if len(value) != 3:
            raise Bot_Exception (bot.send_message(message.chat.id, f'Введено некоректное число параметров, равное {len(value)}, выполните команду /help'))

        base, quote, amount = value[0].lower(), value[1].lower(), value[2]

        if base not in true_value:
            raise Bot_Exception((bot.send_message(message.chat.id, f'Название валюты: {base.upper()} введено некорректно, выполните команду /help')))
        elif quote not in true_value:
            raise Bot_Exception((bot.send_message(message.chat.id, f'Название валюты: {quote.upper()} введено некорректно, выполните команду /help')))
        elif not amount.isdigit():
            raise Bot_Exception((bot.send_message(message.chat.id, f'Количество валюты: {amount.upper()} введено некорректно, выполните команду /help')))
        price = Get_Price.get_price(base, quote, amount)
        bot.send_message(message.chat.id, f'Число {quote} = {price}')

except Exception as e:
        print('Ознакомься с возникшей ошибкой')
else:
    bot.polling(none_stop=True)
