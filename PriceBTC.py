import quandl, datetime, urllib.request, numpy, time
from time import gmtime,strftime
from fractions import Fraction

"""
BCHARTS/BITSTAMPUSD
Visit
https://docs.quandl.com/docs/python-time-series#section-preprocess-the-data
for documentation
and https://blog.quandl.com/api-for-bitcoin-data for more

NOTE: https://plot.ly/python/ for graphing
https://blockchain.info/api/exchange_rates_api for 1 USD to BTC
    Use recripocal for BTC to USD rate
"""
#data = quandl.get("BCHARTS/BITSTAMPUSD", rows=5)
#data = quandl.get("BCHARTS/BITSTAMPUSD", collapse="quarterly")
#print(data)

ref = "https://blockchain.info/tobtc?currency=USD&value=1"
def price():
    response = urllib.request.urlopen(ref)
    data = response.read()
    dataArray = list(str(data))
    rate = ''.join(dataArray[2:12])
    fraction = Fraction(rate)
    recriprocated = numpy.reciprocal(fraction)
    print('One bitcoin equals', float(round(recriprocated, 2)), 'USD')

def ticker():
    for i in range (5):
        price()
        print('Sleeping')
        time.sleep(10)
        
    
