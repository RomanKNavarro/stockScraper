#!/opt/homebrew/bin/python3

''' stockScraper.py: given a ticker, analyze the respective Stock's following info:
    - Company Name
    - EPS
    - P/E Ratio
    - ROE
    - BVPS
    - PBR
    - special "Graham Number"
'''

import bs4
import requests
import math

from colorist import red, ColorRGB

# yahoo finance stock url: https://finance.yahoo.com/quote/ATVIX?.tsrc=fin-srch
# https://finance.yahoo.com/quote/STOCKSYMBOLHERE?.tsrc=fin-srch

red = ColorRGB(200, 0, 0)

while True:
    print("\nINPUT TICKER SYMBOL (OR 'help' FOR HELP)")
    ticker = input().lower()

    url = 'https://stockanalysis.com/stocks/%s/statistics/' % ticker

    res = requests.get(url)

    if ticker != 'help':
        if res.status_code == 200:
            print('(200) ACCESS SUCCESSFUL! (%s)\n' % url)
            mainSoup = bs4.BeautifulSoup(res.text, features="html.parser")  # html parser

            # 1. start off by getting Company name
            name = mainSoup.find('h1')
            print(name.get_text())

            # PRICE
            try:
                price = mainSoup.find('div', class_='text-4xl font-bold inline-block').get_text()
            except AttributeError: 
                # IT SOMETIMES ALTERNATES TO THIS:
                price = mainSoup.find('div', class_='text-4xl font-bold block sm:inline').get_text()

            # for everything else
            stats = mainSoup.find_all('td', class_='px-[5px] py-1.5 text-right font-semibold xs:px-2.5 xs:py-2')

            # EPS
            eps = stats[56].get_text()

            # PE
            pe = stats[10].get_text()

            # ROE
            roe = stats[28].get_text()

            # BVPS
            bvps = stats[62].get_text() 

            # PBR
            priceNum = float(str(price))
            bvpsNum = float(str(bvps))
            pbrNum = priceNum / bvpsNum
            # print(f'PBR: {pbrNum:.2f}')

            epsNum = float(str(eps[1: -1]))
            grahamNum = str(round(math.sqrt(22.5 * epsNum * bvpsNum), 2))
            #print(f'GRAHAM #: {grahamNum:.2f}')

            stats = {"PRICE": price, "EPS": eps, "PE": pe, "ROE": roe, "BVPS": bvps, "GRAHAM #": grahamNum}

            for name, num in stats.items():
                print(name.ljust(20) + num.rjust(20))

        else:
            print('404: Access Denied!')
    else:
        print(f"""
{red}PE:{red.OFF} below 10 is considered low, between 20 & 20 is moderate, 
    and greater than 20 is expensive
    
{red}ROE:{red.OFF} the higher the ROE, the better a company is at converting it's
     equity financing into profits
    
{red}BVPS:{red.OFF} If company's BVPS is higher than it's current stock price, then the
     stock's considered undervaluied.
    
{red}PBR:{red.OFF} value of 1 means that stock's trading in-line w/ BV. Below signals
     a potentially undervalued stock. Above means it's trading @ a premium to the BV.""")