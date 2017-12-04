'''
	bitprice.py is a command line utility that allows you to check bitcoin price from coindesk API.
'''

from urllib import request
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice.json';

def main():
    res = request.urlopen(url)
    if res.getcode() == 200:
        body = res.read();
        json_res = json.loads(body)
        price = json_res['bpi']['USD']['rate_float']
        print('Bitcoin ${}'.format(round(price, 2)))


if __name__ == '__main__':
    main()