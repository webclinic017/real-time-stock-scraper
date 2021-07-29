import requests
import datetime
import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.tradingview.com/symbols/BTCUSDT/')
element = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__main-price.js-scroll-container > div > div > div > div.tv-symbol-price-quote__row.js-last-price-block-value-row > div.tv-symbol-price-quote__value.js-symbol-last')

def real_time_price(ticker):
    url = ('https://www.tradingview.com/symbols/') + ticker + ('/')
    #r = requests.get(url)
    element = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__main-price.js-scroll-container > div > div > div > div.tv-symbol-price-quote__row.js-last-price-block-value-row > div.tv-symbol-price-quote__value.js-symbol-last')
    return element.text

print(driver.title)
print(driver.current_url)
print(element.text)

#web_content = BeautifulSoup(r.text, 'lxml')

list = ['BTCUSDT']

for step in range(1,100000):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for ticker in list:
        price.append(real_time_price(ticker))
    col = [time_stamp]
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time stock data.csv', mode='a', header=False)
    #print(element.text)
    print(col)
    time.sleep(1)