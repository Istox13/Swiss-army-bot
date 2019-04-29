import requests

api_key = 'trnsl.1.1.20190428T170520Z.743fad02911f8bdc.99f8ffbafd35c73417596d593ede2a3f72c748f0'

def translate(l1, l2, phrase):
    translator_uri = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    
    response = requests.get(
        translator_uri,
        params={
            "key":
            # Ключ, который надо получить по ссылке в тексте.
            api_key,
            # Направление перевода: с русского на английский.
            "lang": f"{l1}-{l2}",
            # То, что нужно перевести.
            "text": phrase
        })

    return response.json()["text"][0]

