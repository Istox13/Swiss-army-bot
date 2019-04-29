from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from API_key import key_shwed
from API.expo import EXPO_API
from API.API_traslate import translater
from API.API_ip import search_ip, get_my_ip


def get_list(bot, update):
    update.message.reply_text(EXPO_API.get_list_values())


def get_price(bot, update, args):
    a, b = args[:2]
    list_prices = EXPO_API.get_price(a, b)
    if not list_prices:
        update.message.reply_text('Неверный ввод или информации по данной паре нет')
    else:
        update.message.reply_text(f"""Минимальная цена {list_prices['values'][0]} на бирже: {list_prices['min']} {list_prices['values'][1]}\n
Максимальная цена {list_prices['values'][0]} на бирже: {list_prices['max']} {list_prices['values'][1]}""")


def get_stat(bot, update, args):
    a, b = sorted(args[:2])
    list_prices = EXPO_API.get_stat(a, b)
    if not list_prices:
        update.message.reply_text('Неверный ввод')
    else:
        update.message.reply_text(f"""{list_prices['high']} - максимальная цена сделки за 24 часа;
{list_prices['low']} - минимальная цена сделки за 24 часа;
{list_prices['last_trade']} - цена последней сделки;
{list_prices['buy_price']} - текущая максимальная цена покупки;
{list_prices['sell_price']} - текущая минимальная цена продажи.""")


def start(bot, update):
    update.message.reply_text(
        "Привет! Я швейцарский-бот. Напиши /help что-бы узнать поподробнее.")


def help(bot, update):
    update.message.reply_text(
        """Доступные команды:
/help - помощь 
/список_валют
/книга_ордеров_по_валютной_паре <валюта_1> <валюта_2> 
/статистика_цен_по_валютной_паре <валюта_1> <валюта_2> 
/переведи <текст> - переводит с любого языка на русский и с русского на английский
/вычисли_по_ip <ip> - выводит информацию о ip""")

def echo(bot, update):
    pass


def main():
    updater = Updater(key_shwed)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('список_валют', get_list))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('книга_ордеров_по_валютной_паре', get_price, pass_args=True))
    dp.add_handler(CommandHandler('статистика_цен_по_валютной_паре', get_stat, pass_args=True))
    dp.add_handler(CommandHandler('переведи', translater, pass_args=True))
    dp.add_handler(CommandHandler('мой_ip', get_my_ip))
    dp.add_handler(CommandHandler('вычисли_по_ip', search_ip, pass_args=True, pass_chat_data=True))
    

    updater.start_polling()

    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    print('Bot ON')
    main()