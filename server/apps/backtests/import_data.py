import yfinance as yf

data = yf.download("SPY", start="1999-05-01", end="2019-10-04")
data.to_csv("csv/spy.csv")
