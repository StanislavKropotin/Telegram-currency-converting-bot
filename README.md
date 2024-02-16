# Telegram-currency-converting-bot
The bot returns the price for a certain amount of currency (list of currencies in the "Config.py" file).
I used the "pytelegrambotapi" library.
To get the exchange rate I used the API (requests are sent using the Requests library).
JSON is used for parsing.
Exceptions have been written so that if the user blocks something that is not there, an error message is displayed and the bot does not stop working.
Exceptions, dictionary and token are placed in separate files.
