from django.shortcuts import render, redirect
from apps.charts.functions import *
import yfinance as yf

def HomeView(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        return redirect('crypto/')

    context = {

    }
    return render(request, 'charts/index.html', context)


def CryptoView(request):

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
