''' stockScraper.py: given a ticker, analyzes the respective Stock's following info:
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

# yahoo finance stock url: https://finance.yahoo.com/quote/ATVIX?.tsrc=fin-srch
# https://finance.yahoo.com/quote/STOCKSYMBOLHERE?.tsrc=fin-srch

while True:
    print("\nINPUT TICKER SYMBOL")
    ticker = input().lower()

    url = 'https://stockanalysis.com/stocks/%s/statistics/' % ticker

    res = requests.get(url)

    if res.status_code == 200:
        print('(200) ACCESS SUCCESSFUL! (%s)\n' % url)
        mainSoup = bs4.BeautifulSoup(res.text, features="html.parser")  # html parser

        # 1. start off by getting Company name
        name = mainSoup.find('h1')
        print(name.get_text())

        price = mainSoup.find('div', class_='text-4xl font-bold inline-block').get_text()

        stats = mainSoup.find_all('td', class_='px-[5px] py-1.5 text-right font-semibold xs:px-2.5 xs:py-2')

        # PRICE
        print('PRICE: %s' % price)

        # EPS
        eps = stats[56].get_text()
        print('EPS: %s' % eps)

        # PE
        pe = stats[10].get_text()
        print('P/E RATIO: %s' % pe)

        # ROE
        roe = stats[28].get_text()
        print('ROE: %s' % roe)

        # BVPS
        bvps = stats[62].get_text()
        print('BVPS: %s' % bvps)

        # PBR
        priceNum = float(str(price))
        bvpsNum = float(str(bvps))
        print(f'PBR: {(priceNum / bvpsNum):.2f}')

        # GRAHAM NUMBER
        # sqrt(22.5 * eps * bvps)

        epsNum = float(str(eps[1: -1]))
        grahamNum = math.sqrt(22.5 * epsNum * bvpsNum)
        print(f'GRAHAM #: {grahamNum:.2f}')

    else:
        print('404: Access Denied!')



    #     # scraping logic:
    #     mainSoup = bs4.BeautifulSoup(res.text, features="html.parser")  # html parser

    #     # 1. start off by getting Company name
    #     # nameElem = mainSoup.select('.D(ib) Mend(20px)')
    #     results = mainSoup.find(id='atomic')
    #     name = results.find_all('title')  # element type goes in here
    #     print(name[0].text[0])


    # res.raise_for_status()
