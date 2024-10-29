import requests as rq

cUrl = 'https://api.coinbase.com/v2/exchange-rates?currency=USD'


cHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

stockData = [
    {
        'name':'TCS',
        'current_price': 3000,
        'currency': 'INR',
        'price': '?'
    },
        {
        'name':'GOOG',
        'current_price': 166.82,
        'currency': 'USD',
        'price': '?'
    },
    {
        'name':'DBS_GROUP',
        'current_price': 39.18,
        'currency': 'SGD',
        'price': '?'
    }
]

cResp = rq.get(url=cUrl, headers= cHeader)

jResp = cResp.json()

currencyData=jResp['data']['rates']

#print('currencyData',currencyData)

def convert_currency(currencyData):
  for stock in stockData:
    currency=stock['currency']
    rate = stock['current_price']

    if currency =='INR':
        usd_rate = float(currencyData['INR'])
        stock['price'] = round(rate/usd_rate,2)

    elif currency=='USD':
        inr_rate=float(currencyData['INR'])
        stock['price']=round(rate * inr_rate,2)
        
    elif currency == 'SGD':
            Inr_rate = float(currencyData['INR'])
            stock['price'] = round(rate* Inr_rate,2)

    # elif currency in currencyData:
    #         stock['price'] = round(rate * rate, 2)
    else:
          stock['price']='error'

convert_currency(currencyData)

for stock in stockData:
    print(f'name = {stock['name']},current_price = {stock['current_price']},currency = {stock['currency']},price = {stock['price']}')



