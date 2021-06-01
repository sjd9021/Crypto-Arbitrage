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


def get_price_bns():
    usdt = bitbnsObj.getTickerApi('USDT')
    price_bitbns = (usdt['USDT']['last_traded_price'])
    return price_bitbns


def send_message(chat_id, msg, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
# send the msg
    requests.get(url)


def wazir():
    dict1 = {}
    url =  'https://api.wazirx.com/api/v2/tickers'
    response = requests.get(url)
    data2 = response.json()
    return (data2['usdtinr']['last'])

def main():
    spread_list = []

    while True:

        pricebns = get_price_bns()
        pricedcx = get_price_dcx()
        pricewazir = float(wazir())

        if pricewazir < 76.2:
            send_message(
                chat_id=1340763512,
                msg=f'USDT price in wazir is {pricewazir}',
                bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
        print(pricebns, pricedcx)
        if pricedcx > pricebns:
            spread = ((pricedcx - pricebns) / pricebns) * 100
        else:
            spread = ((pricebns - pricedcx) / pricedcx) * 100

        spread_list.append(spread)
        print(spread)
        time_interval = 60 * 3
        # if spread > 0.6:
        #     time_interval = 60
        #     if pricedcx > pricebns:
        #         send_message(
        #             chat_id=1340763512,
        #             msg=f'USDT spread is {spread} Go buy in Bitbns',
        #             bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
        #         send_message(
        #             chat_id=1200858304,
        #             msg=f'USDT spread is {spread} Go buy in Bitbns',
        #             bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
        #     else:
        #         send_message(
        #             chat_id=1340763512,
        #             msg=f'USDT spread is {spread} Go buy in Bitdcx',
        #             bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
        #         send_message(
        #             chat_id=1200858304,
        #             msg=f'USDT spread is {spread} Go buy in Bitdcx',
        #             bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
        # else:
        #     time_interval = 3*60
        # if len(spread_list) > 20:
        #     send_message(
        #         chat_id=1340763512,
        #         msg=spread_list,
        #         bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')
        #     send_message(
        #         chat_id=1200858304,
        #         msg=spread_list,
        #         bot_token='1816688031:AAFHkK0ZffO9BXtd-nS6NaCL6UP3SV_JSZs')
        #     spread_list = []
            # empty the price_list

        time.sleep(time_interval)


main()

