import requests
import json

class EXMO_API:
    def get_list_values():
        values = requests.get('https://api.exmo.com/v1/currency/').json()
        
        return ', '.join(values)

    def get_price(a, b):
        a, b = [a, b]
        ls = requests.get('https://api.exmo.com/v1/currency/').json()
        values = [a, b]

        if a not in ls or b not in ls:
            return False
        else:
            zapr = requests.get(f'https://api.exmo.com/v1/order_book/?pair={a}_{b}').json()

            if not zapr.values():
                zapr = requests.get(f'https://api.exmo.com/v1/order_book/?pair={b}_{a}').json()
                print(zapr)
                values = [b, a] 
                if not zapr:
                    return False 
                zapr = zapr[f'{values[0]}_{values[1]}']
                return {'max': str(1 / float(zapr['ask_top'])), 'min': str(1 / float(zapr['bid_top'])), 'values': values[::-1]}

            zapr = zapr[f'{values[0]}_{values[1]}']
            print(zapr)
            return {'max': zapr['ask_top'], 'min': zapr['bid_top'], 'values': values}

    def get_stat(a, b):
        list_stat = requests.get('https://api.exmo.com/v1/ticker/').json()
       
        a, b = a.upper(), b.upper()
        val = f'{a}_{b}'

        if val not in list_stat:
            val = f'{b}_{a}'

            if val not in list_stat:
                return False

        list_stat = list_stat[val] 

        return list_stat


            