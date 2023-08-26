import requests
import json
from Config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            keys[base] = keys[base]
        except KeyError:
            return APIException(f"Вы указали валюты не из предоставленного списка, возможно опечатались, проверьте корректность ввода и попробуйте заново!")
        try:
            keys[quote] = keys[quote]
        except KeyError:
            return APIException(f"Вы указали валюты не из предоставленного списка, возможно опечатались, проверьте корректность ввода и попробуйте заново!")
        if keys[base] == keys[quote]:
            raise APIException(f'Вы указали одинаковые валюты, перевод невозможен!')
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f"Не удалось обработать колличество {amount}!")

        r = requests.get(f"https://v6.exchangerate-api.com/v6/711159da9adb409f31b18ace/pair/{keys[quote]}/{keys[base]}/{amount}")
        resp = json.loads(r.content)
        new_price = resp["conversion_result"]
        new_price = round(new_price, 3)
        message = f'Цена {amount} {keys[quote]} в {keys[base]}: {new_price}'
        return message