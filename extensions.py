import requests  # импортируем наш знакомый модуль
from requests.exceptions import HTTPError
import lxml.html
from lxml import etree
import os

# Считыватель токена телеграм бота

class Read_Token:
    def read_token():
        path_file = r'C:\Users\TASMaster\Desktop\Bot_Token.txt'
        try:
            with open(path_file, 'r') as token:
                bot_token = token.readline()

        except FileNotFoundError as e:
            return print('Ошибка!!! Файл с токеном не найден.')

        else:
            if os.stat(path_file).st_size == 0:
                return print('Ошибка!!! Токен отсутсвует в файле.')
            else:
                return bot_token

# Парсер HTML для получения курса валюты
class Get_Rate():
    @staticmethod
    def get_rate(rate):
        URL = r'https://www.cbr.ru/currency_base/daily/'
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        try:
            r = requests.get(URL, headers = HEADERS).content

        except HTTPError as http_err:
            print(f'HTTP произошла ошибка: {http_err}')

        else:
            tree = lxml.html.document_fromstring(r)
            if rate == 'доллар':
                USD = tree.xpath('/html/body/main/div/div/div/div[3]/div/table/tbody/tr[12]/td[5]/text()')
                USD_ = float(USD[0].replace(',', '.'))
                return USD_

            elif rate == 'евро':
                EUR = tree.xpath('/html/body/main/div/div/div/div[3]/div/table/tbody/tr[13]/td[5]/text()')
                EUR_ = float(EUR[0].replace(',', '.'))
                return EUR_

# Конвертер валют
class Get_Price:
    @staticmethod
    def get_price(base, quote, amount):
        if (base == 'доллар' or base == 'евро') and quote == 'рубль':
            base_ = Get_Rate.get_rate(base)
            price = base_ * float(amount)
            return price

        elif base == 'рубль' and (quote == 'доллар' or quote == 'евро'):
            quote_ = Get_Rate.get_rate(quote)
            price = float(amount) / quote_
            return price

        elif (base == 'доллар' or base == 'евро') and (quote == 'доллар' or quote == 'евро'):
            base_ = Get_Rate.get_rate(base)
            quote_ = Get_Rate.get_rate(quote)
            price = (base_ * float(amount)) / quote_
            return price
class Bot_Exception(Exception):
    pass

if __name__ == '__main__':
    print(Read_Token.read_token())
    print(Get_Rate.get_rate('USD'))
    print(Get_Rate.get_rate('EUR'))
    print(Get_Price.get_price('USD', 'RUB', 100))