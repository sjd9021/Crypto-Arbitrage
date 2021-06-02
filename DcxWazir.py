import requests
import time

time_interval = 3 * 60

def wazir():
    dict1 = {}
    url =  'https://api.wazirx.com/api/v2/tickers'
    response = requests.get(url)
    data2 = response.json()
    xrp_waxir = float(data2['xrpinr']['last'])
    xlm_waxir = float(data2['xlminr']['last'])
    trx_wazir = float(data2['trxinr']['last'])
    price_wazir = [xrp_waxir, xlm_waxir, trx_wazir]
    return price_wazir

def get_price_dcx():
    url = ["https://public.coindcx.com/market_data/trade_history?pair=B-XRP_USDT",
           "https://public.coindcx.com/market_data/trade_history?pair=B-XLM_USDT",
           "https://public.coindcx.com/market_data/trade_history?pair=B-TRX_USDT"]
    usdt = "https://public.coindcx.com/market_data/trade_history?pair=I-USDT_INR&limit=50"
    response = requests.get(usdt)
    data = response.json()
    price_dcx = (data[1]["p"])
    dcx = []
    for i in url:
        response = requests.get(i)
        data = response.json()
        price = float(data[1]["p"])
        price = price * price_dcx
        dcx.append(price)

    return dcx

def concat():
    price_wazirx = wazir()
    pricedcx = get_price_dcx()

    difference = []


    zip_object = zip(pricedcx, price_wazirx)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i-list2_i)

    dict = {"xrp" : difference[0],"xlm" : difference[1], "trx" : difference[2]}

    return dict

def send_message(chat_id, msg, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
# send the msg
    requests.get(url)

def main():

    while True:
        dictionary = concat()
        for price in dictionary:
            if dictionary[price] < 0.1:
                send_message(
                    chat_id=1340763512,
                    msg=f'the difference in price of {price} is {dictionary[price]} can transfer funds',
                    bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')

        time.sleep(time_interval)

main()