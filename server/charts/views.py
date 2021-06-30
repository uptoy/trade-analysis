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
    return render(request, '/crypto.html', context)


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
