from bs4 import BeautifulSoup
import json
import requests
import logging

logger = logging.getLogger(__name__)

class YahooTracker:
    ticker_cnt = 0

    def __init__(self):
        print('Creating yahoo tracker')
        self.ticker_list = []
    
    def _is_tracked(self, ticker):
        return any(t.symbol == ticker.symbol for t in self.ticker_list)

    def add_ticker(self, ticker):
        """ Add ticker to tracking if not already in list"""
        if not _is_tracked(ticker):
            logger.info(f"Added {ticker.symbol} to tracker")
            ticker_cnt += 1
            self.ticker_list.append(ticker)

if __name__ == '__main__':
    URL = 'https://finance.yahoo.com/quote/AMZN/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='quote-summary')
    #print(results.prettify())
    
    print(f'type: {type(results)}, count: {len(results)}')

    for elem in results:
        print(f"type: {type(elem)}")
        print(f"data-test: {elem.get('data-test')}")
        print(f"ID: {elem.get('id')}")
        print(f"Name: {elem.get('id')}")

    tables = soup.find(id='quote-summary').find_all('table')
    print(f"tables: {type(tables)}")
    for table in tables:
        quote_summary_td = table.find_all('td')

        for i,td in enumerate(quote_summary_td,start=1):

            # Check if this <td> has an inner span, and if so display those contents 
            #print(f"{i} - {td.contents} -> {td.string}")
            td_text = td.string if td.string is not None else td.contents

            # even column is the title
            # odd is the value

            # Need to figure out how to traverse ALL span elements
            if i % 2 == 0:
                end = '\n'
            else:
                td_text += ':'
                end = ''
            print(f"{td_text}",end=end)

