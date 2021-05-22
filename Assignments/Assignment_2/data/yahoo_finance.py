import yfinance as yf
import pandas as pd


stock_ticker_list = pd.read_csv('Stock_Ticker_List.csv')


for stock in stock_ticker_list['Symbol']:
    yf.download(stock).to_csv('raw/' + stock + '.csv')
    print(stock, 'finished')

