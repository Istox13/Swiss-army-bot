import requests
from langdetect import detect

api_key = 'trnsl.1.1.20190428T170520Z.743fad02911f8bdc.99f8ffbafd35c73417596d593ede2a3f72c748f0'


def translater(bot, updater, args):
    text = ' '.join(args)
    text_lang = detect(text)

    accompanying_text = "Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru/."
    translator_uri = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    
    response = requests.get(
        translator_uri,
        params={
            "key":
            # Ключ, который надо получить по ссылке в тексте.
            api_key,
            # Направление перевода: с русского на английский.
            "lang": f"{text_lang}-{'ru' if text_lang != 'ru' else 'en'}",
            # То, что нужно перевести.
            "text": text  
        })

    updater.message.reply_text(
        "\n\n".join([response.json()["text"][0], accompanying_text]))