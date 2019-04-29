import requests
from langdetect import detect


def search_ip(bot, updater, args):
    ip = args[0]
    response = requests.get(
        f'http://api.ipstack.com/{ip}',
        params={
            "access_key": 'db3b9923709f28537f45d316d444f4d3'
        }).json()

    updater.message.reply_text(f"""IP: {response['ip']} {response['location']['country_flag_emoji']}
Тип IP адреса: {response['type']} 
Континент: {response['continent_name']}
Страна: {response['country_name']}
Регион: {response['region_name']}
Город: {response['city']}
""")


def get_my_ip(bot, updater):
    updater.message.reply_text(f"Ваш ip можно узнать перейдя по ссылке: https://api.ipify.org?format=json")
    