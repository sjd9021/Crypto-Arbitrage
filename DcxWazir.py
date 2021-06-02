import requests
import time

time_interval = 3 * 60

def wazir():
    dict1 = {}
    url =  'https://api.wazirx.com/api/v2/tickers'
    response = requests.get(url)
    data2 = response.json()
    xrp_waxir = float(data2['xrpinr']['last'])*0.998
    xlm_waxir = float(data2['xlminr']['last'])*0.998
    trx_wazir = float(data2['trxinr']['last'])*0.998
    price_wazir = [xrp_waxir, xlm_waxir, trx_wazir]
    return price_wazir

def get_price_dcx():
    url = ["https://public.coindcx.com/market_data/trade_history?pair=B-XRP_USDT",
           "https://public.coindcx.com/market_data/trade_history?pair=B-XLM_USDT",
           "https://public.coindcx.com/market_data/trade_history?pair=B-TRX_USDT"]
    usdt = "https://public.coindcx.com/market_data/trade_history?pair=I-USDT_INR&limit=50"
    response = requests.get(usdt)
    data = response.json()
    price_dcx = (data[1]["p"])*1.001
    dcx = []
    for i in url:
        response = requests.get(i)
        data = response.json()
        price = float(data[1]["p"]) * 1.001
        price = price * price_dcx
        dcx.append(price)

    return dcx

def concat():
    price_wazirx = wazir()
    pricedcx = get_price_dcx()
    print(pricedcx)
    print(price_wazirx)
    difference = []


    zip_object = zip(pricedcx, price_wazirx)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i-list2_i)
    print(difference)
    for i in range(3):
        difference[i] = (difference[i]/pricedcx[i])*100

    dict = {"xrp" : difference[0],"xlm" : difference[1], "trx" : difference[2]}
    print(dict)
    return dict

def send_message(chat_id, msg, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
# send the msg
    requests.get(url)

def main():

    while True:
        dictionary = concat()
        for price in dictionary:
            if dictionary[price] < 0:
                send_message(
                    chat_id=1340763512,
                    msg=f'the difference in price of {price} is {dictionary[price]}% can transfer funds',
                    bot_token='1868431736:AAFE410MUEsn1hfbR6PB1LT6QiF_A2l1280')

        time.sleep(time_interval)


main()