#!/usr/bin/python3

# Financial web scraper
# scrape from yahoo finance
# use bs4

from bs4 import BeautifulSoup
import requests

# funcion to scrape for news in yahoo finance
def yahoo_finance_news_scraper(ticker):
    # get url
    url = f'https://finance.yahoo.com/quote/{ticker}/'

    # send request and get response
    response = requests.get(url)

    try:
        # error checking
        response.raise_for_status()
        # get the contents
        contents = BeautifulSoup(response.text, "html.parser")

        # get news section, and extract a list of news
        newsList = contents.find_all('section', attrs={"data-testid": "storyitem"})

        # for every news in newslist, print the news headline (title)
        print(f'--- Recent News of {ticker} ---')
        printed_news = []
        for news in newsList:
            news_title = news.find('a')['title']
            if not news_title in printed_news:
                printed_news.append(news_title)
                print(news_title)

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

# main
def main():
    # get input(ticker)
    ticker = input("Please enter stock ticker:\n")
    # call yahoo scraper
    yahoo_finance_news_scraper(ticker)

if __name__ == "__main__":
    main()

