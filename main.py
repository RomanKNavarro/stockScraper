''' stockScraper.py: given a ticker, analyzes the respective Stock's following info:
    - Company Name
    - EPS
    - P/E Ratio
    - ROE
    - BVPS
    - PBR
    - special "Graham Number"
'''

# from bs4 import BeautifulSoup 
import bs4
import requests

# yahoo finance stock url: https://finance.yahoo.com/quote/ATVIX?.tsrc=fin-srch
# https://finance.yahoo.com/quote/STOCKSYMBOLHERE?.tsrc=fin-srch

while True:
    print("INPUT TICKER SYMBOL")
    ticker = input().upper()
    url = 'https://finance.yahoo.com/quote/%s?.tsrc=fin-srch' % ticker
    print(url)

    res = requests.get(url)
    print(res.status_code)  # 200 if successful

    if res.status_code == 200:
        print('(200) ACCESS SUCCESSFUL!: %s\n' % url)

        # scraping logic:
        mainSoup = bs4.BeautifulSoup(res.text, features="html.parser")  # html parser

        # 1. start off by getting Company name
        # nameElem = mainSoup.select('.D(ib) Mend(20px)')
        # print(nameElem[1])

        results = mainSoup.find(id='atomic')
        name = results.find_all('title')
        print(name[0].text[0:])


    # res.raise_for_status()
