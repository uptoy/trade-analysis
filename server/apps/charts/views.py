from django.shortcuts import render, redirect
from django.http import HttpResponse
import environ

# most dependencies and imports made in functions.py to avoid clutter
from .functions import *

env = environ.Env()
env.read_env('.env')


def index(request):
    return HttpResponse("charts")


def homeView(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        return redirect('crypto/')

    context = {

    }
    return render(request, 'charts/index.html', context)


def cryptoView(request):

    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        symbol = symbol.upper()
    else:
        symbol = 'BTCUSD'

    data = spotquote(symbol)
    pricedata = pricechange(symbol)
    moredata = pricechange(symbol)

    # get a fricken df
    ts_df = candles(symbol)
    # PlotlyGraph

    def candlestick():
        figure = go.Figure(
            data=[
                go.Candlestick(
                    x=ts_df.index,
                    high=ts_df['high'],
                    low=ts_df['low'],
                    open=ts_df['open'],
                    close=ts_df['close'],
                )
            ]
        )

        candlestick_div = plot(figure, output_type='div')
        return candlestick_div
    # endPlotlyGraph
    percentchange = pricedata['priceChangePercent']
    buyers = pricedata['askQty']
    sellers = pricedata['bidQty']

    eth = pricechange(symbol='ETHUSD')
    btc = pricechange(symbol="BTCUSD")
    ltc = pricechange(symbol="LTCUSD")

    context = {
        'moredata': moredata,
        'eth': eth,
        'btc': btc,
        'ltc': ltc,
        'percentchange': percentchange,
        'buyers': buyers,
        'sellers': sellers,
        'data': data,
        'candlestick': candlestick(),
    }
    return render(request, 'charts/crypto.html', context)


"""
from django.http import HttpResponse
import yfinance as yf
import plotly
import pandas as pd
import requests
import json
import csv
import environ
import plotly.graph_objects as pg

env = environ.Env()
env.read_env('.env')


def index(request):
    return HttpResponse("charts")


def yahoo(request):
    slack = yf.Ticker("WORK")
    history = slack.history(period="max")
    history.to_csv
    return HttpResponse("create csv")


def iexcloud():
    TOKEN = env('TOKEN')
    # or TOKEN = env.get_value('TOKEN',str)
    SYMBOL = 'AAPL'
    URL = 'https://sandbox.iexapis.com/stable/stock/{}/chart/max?token={}', format(SYMBOL, TOKEN)
    r = requests.get(URL)
    json_data = json.loads(r.content)

    csv_file = open('stock.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['date', 'open', 'high', 'low', 'close'])

    for item in json_data:
        print(item)
        csv_writer.writerow(item['date'], item['open', item['high'], item['low'], item['close']])
    csv_file.close()


iexcloud()


def view_chart(request):
    df = pd.read_csv('stock.csv')
    candlestick = pg.Candlestick(
        x=df[date],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'])
    fig = pg.Figure(data=[candlestick])
    fig.layout.xaxis.type = 'category'
    # figure.show()
    shapes = [
        dict(x0='2019-01-02', x1='2019-01-02', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2019-05-05', x1='2019-05-05', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2019-07-30', x1='2019-07-30', y0=0, y1=1, xref='x', yref='paper'),
        dict(x0='2019-10-30', x1='2019-10-30', y0=0, y1=1, xref='x', yref='paper'),
    ]

    annotations = [
        dict(
            x='2019-01-03',
            y=0.01,
            xref='x',
            yref='paper',
            showarrow=False,
            xanchor='left',
            text='Apple Cuts Guidance'),
        dict(x='2019-05-05', y=0.5, xref='x', yref='paper', showarrow=False, xanchor='left', text='Trump Tariff Tweet'),
        dict(x='2019-07-30', y=0.3, xref='x', yref='paper', showarrow=False,
             xanchor='left', text='Trump Tweets "China is doing very badly"'),
        dict(x='2019-10-30', y=0.3, xref='x', yref='paper', showarrow=False, xanchor='left', text='Apple Q4 Earnings'),
    ]
    fig.update_layout(title='AAPL', annotations=annotations, shapes=shapes)
    fig.show()
    fig.write_html('aapl.html', auto_open=False)

"""



# RSI

# MACD

# BB

# SMA

# EMA

# STOCH

# Volume

# CC


"""
import os
import csv
from django.http import HttpResponse
import pandas as pd
import io
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# バックエンドを指定
matplotlib.use('Agg')

# グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化


def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数


def get_svg(request):
    setPlt()
    svg = plt2svg()  # SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response




def index(request):
    return HttpResponse("indicators")


def index2(request):
    my_context = {
        "text": "test",
        "true": True,
        "number": 123,
        "list": [1, 2, 3],
    }
    return render(request, "index2.html", my_context)
    # {{text}}{{true}}


def index3(request):
    obj = ProductModel.objects.get(id=1)
    context = {
        "title": obj.title,
        "desc": obj.desc,
        "object": obj
    }
    return render(request, "index3.html", context)
    # html {{text}}{{desc}}{{object}}{{object.title}}
    # html {%  if obj.desc !=None and obj.desc !='' %}{{obj.desc}}{% else %}description coming soon{% endif %}
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)  # form からPOSTしたデータを表示する


def index4(request):
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        context = {
            "form": my_form
        }
        return render(request, "index4", context)


def predict(request):
    # Visualize the close price data
    df = pd.readcsv("csv/FB_1D_1Y.csv")
    plt.figure(figsize=(16, 8))
    plt.title("FB_Daily")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.plot(df["Close"])
    plt.show()

    # Create a variable to predict 'x' days out into the future
    future_days = 25
    df['Prediction'] = df[["Close"]].shift(-future_days)

    # Create the feature data set(X) and convert it to a numpy array and remove the last 'x' rows/days
    X = np.array(df.drop(['Prediction'], 1))[:future_days]
    # Create the target data set (Y) and convert it to a numpy array and get
    # all of the target values except the last "X" rows
    y = np.array(df['Prediction'])[:future_days]

    X_train, x_test, Y_train, y_test = train_test_split(X, y, test_size=0.25)
    # Create the models
    # Create the decision tree regressor model
    tree = DecisionTreeRegressor().fit(x_train, y_train)
    # Create the liner regression model
    lr = LinearRegression().fit(x_train, y_train)
    # Get the last "x" row of the feature date set
    x_future = df.drop(['Prediction'], 1)[:-future_days]
    x_future = x_future.tail(future_days)
    x_future = np.array(x_future)
    # Show the model tree prediction
    lr_prediction = lr.predict(x_future)
    # Visialize the date
    predictions = tree_prediction
    valid = df[X.shape[0]:]
    valid["Predictions"] = predictions
    plt.figure(figsize=(16, 8))
    plt.title("Model")
    plt.xlabel("days")
    plt.ylabel("usd")
    plt.plot(df['Close'])
    plt.plot(valid[["Close", "Predictions"]])
    plt.legend(["Orig", "Val", "Pred"])
    plt.show


def setPlt2():
    df = pd.read_csv('csv/FB_1D_1Y.csv')
    print(df['Close'])
    print(df['Date'])
    y = df['Close']
    x = df['Date']
    plt.title("FB_Daily", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("Close Price USD($)")
    plt.plot(x, y, color='#00d5ff')
    fig = plt.figure(figsize=(120, 80))
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    plt.show()


# SVG化
def plt2svg2():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数


def get_svg2(request):
    setPlt2()
    svg = plt2svg()  # SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
"""

# try catch
"""
try:
    f = open('file.txt')
    if f.name == 'file.txt':
        raise Exception
except Exception as e:
    print(e)
except FileNotFoundError as e:
    print("error")
else:
    print(f.read())
    f.close()
finally:
    print("finally message")
"""

#　乗数計算
"""
def square_numbers(nums):
    for i in nums:
    yield(i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)

# result
1
4
9
16
25
"""
