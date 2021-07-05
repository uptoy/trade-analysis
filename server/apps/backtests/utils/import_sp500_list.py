import yfinance as yf
import csv


campanies = csv.reader(open('../csv/sp500_companies.csv'))

for campany in campanies:
    # print(company)
    symbol, name = campany

    history_finance = '../csv/{}.csv'.format(symbol)

    f = open(history_finance, 'w')
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")
    f.write(df.to_csv())

    f.close()
