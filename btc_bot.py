import time
import requests


def get_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['bitcoin']['usd']


while True:
    price = get_btc_price()
    print(f"Current BTC Price: ${price}")

    if price > 70000:
        print("🚨 Bitcoin is ABOVE $70,000!")
    elif price < 60000:
        print("⚠️ Bitcoin is BELOW $60,000!")

    time.sleep(300)
