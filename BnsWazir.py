import requests
import time

from bitbnspy import bitbns
from collections import OrderedDict

key = 'AD4CAA35418E236E04FECAA77A424EB1'
secretKey = '16A1FB191F7347EFD8CF3427A2D18C0E'
bitbnsObj = bitbns(key, secretKey)
def funct():
    dict2 = {}
    price = bitbnsObj.getTickerApi('')
    price = OrderedDict(sorted(price.items()))
    for pr in price:
        price_bitbns = (price[pr]['last_traded_price'])
        d = {pr: price_bitbns}
        dict2.update(d)
    return (dict2)




def wazir():
    dict1 = {}
    url =  'https://api.wazirx.com/api/v2/tickers'
    response = requests.get(url)
    data2 = response.json()
    data2 = OrderedDict(sorted(data2.items()))
    for data in data2:
      price_wazir = (data2[data]['last'])
      if 'inr' in data:
          d = {data[:-3].upper():price_wazir}
          dict1.update(d)
    return dict1

dataset1 = wazir()
dataset2 = funct()
a=[]
for key in dataset1.keys():
    if not key in dataset2:
        a.append(key)
for i in a:
    del dataset1[i]
b=[]

for key in dataset2.keys():
    if not key in dataset1:
        b.append(key)

for i in b:
    del dataset2[i]
g = {}
print(dataset2)
print(dataset1)
x =0
for i in dataset1:
    x = float(dataset2[i])
    y = float(dataset1[i])
    if y > 0.0:
        x = ((x-y)/y) * 100
        d = {i:x}
        g.update(d)

sorted_tuples = sorted(g.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

for i in sorted_dict:
    print(i, " ", sorted_dict[i])
