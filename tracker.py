import requests
import time

from bitbnspy import bitbns

key = 'AD4CAA35418E236E04FECAA77A424EB1'
secretKey = '16A1FB191F7347EFD8CF3427A2D18C0E'
bitbnsObj = bitbns(key, secretKey)
threshold = 30000


def get_price_dcx():
    url = "https://public.coindcx.com/market_data/trade_history?pair=I-USDT_INR&limit=50"
    response = requests.get(url)
    data = response.json()
    price_dcx = (data[1]["p"])
    return price_dcx

def get_price_matic_dcx():
    url = "https://public.coindcx.com/market_data/trade_history?pair=I-MATIC_INR&limit=50"
    response = requests.get(url)
    data = response.json()
    price_dcx = (data[1]["p"])
    return price_dcx

def get_price_bns():
    usdt = bitbnsObj.getTickerApi('USDT')
    price_bitbns = (usdt['USDT']['last_traded_price'])
    return price_bitbns

def get_price_matic_bns():
    usdt = bitbnsObj.getTickerApi('MATIC')
    price_bitbns = (usdt['MATIC']['last_traded_price'])
    return price_bitbns

def spread_usdt():
    pricebns = get_price_bns()
    pricedcx = get_price_dcx()
    if pricedcx > pricebns:
        spread = ((pricedcx - pricebns) / pricebns) * 100
    else:
        spread = ((pricebns - pricedcx) / pricedcx) * 100

    return spread

def spread_matic():
    pricebns = get_price_matic_bns()
    pricedcx = get_price_matic_dcx()
    if pricedcx > pricebns:
        spread = ((pricedcx - pricebns) / pricebns) * 100
    else:
        spread = ((pricebns - pricedcx) / pricedcx) * 100

    return spread

def inform(c,difference):
    if c == "USDT":
        pricebns = get_price_bns()
        pricedcx = get_price_dcx()
        spread = spread_usdt()
    else:
        pricebns = get_price_matic_bns()
        pricedcx = get_price_matic_dcx()
        spread = spread_matic()

    if spread > difference:
        if pricedcx > pricebns:
            send_message(
                chat_id=1340763512,
                msg=f'{c} spread is {spread} Go buy in Bitbns',
                bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
            send_message(
                chat_id=1200858304,
                msg=f'{c} spread is {spread} Go buy in Bitbns',
                bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
            return 60
        else:
            send_message(
                chat_id=1340763512,
                msg=f'{c} spread is {spread} Go buy in Coindcx',
                bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
            send_message(
                chat_id=1200858304,
                msg=f'{c} spread is {spread} Go buy in Coindcx',
                bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
            return 60
    return 3 * 60




def send_message(chat_id, msg, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
# send the msg
    requests.get(url)


def main():
    spread_list = []

    while True:

        pricebns = get_price_bns()
        pricedcx = get_price_dcx()

        matic_dcx = get_price_matic_dcx()
        matic_bns = get_price_matic_bns()

        time_interval = 180
        print(pricebns, pricedcx)
        spread = spread_usdt()
        spread_list.append(spread)
        print(spread)
        x = inform("USDT", 0.6)
        x = inform("MATIC", 3.5)
        spread2 = spread_matic()


        if len(spread_list) > 20:
            send_message(
                chat_id=1340763512,
                msg=spread_list,
                bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
            send_message(
                chat_id=1200858304,
                msg=spread_list,
                bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
            spread_list = []


        time.sleep(time_interval)


main()

