"""
売買タイミング:月末
売買シグナル:200日移動平均線を上回るとき持ち金の98%でSPYを購入する
          :200日移動平均線を下回るとき全て売却する
"""

import pandas
import pandas_market_calendars as market_calendar
from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma
from pyalgotrade import plotter
from pyalgotrade.stratanalyzer import returns, drawdown, trades
import matplotlib as mpl
import matplotlib.pyplot as plt

# get last days of month
nyse = market_calendar.get_calendar('NYSE')
df = nyse.schedule(start_date='2000-01-01', end_date='2019-12-31')
df = df.groupby(df.index.strftime('%Y-%m')).tail(1)
df['date'] = pandas.to_datetime(df['market_open']).dt.date
last_days_of_month = [date.isoformat() for date in df['date'].tolist()]


class MovingAverageStrategy(strategy.BacktestingStrategy):

    def __init__(self, feed, instrument):
        super(MovingAverageStrategy, self).__init__(feed)
        self.instrument = instrument
        self.position = None
        self.ma = ma.SMA(feed[instrument].getAdjCloseDataSeries(), 200)
        self.setUseAdjustedValues(True)

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.info(f"==== BUY at {execInfo.getPrice()} {execInfo.getQuantity()}====")
        # self.info(f"{position.getEntryOrder().getExecutionInfo()}")

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.info(f"==== SELL at {execInfo.getPrice()} ====")
        # self.info(f"{position.getEntryOrder().getExecutionInfo()}")
        self.position = None

    def onBars(self, bars):
        if self.ma[-1] is None:
            return

        bar = bars[self.instrument]
        close = bar.getAdjClose()
        date = bar.getDateTime().date().isoformat()

        if date in last_days_of_month:
            if self.position is None:
                broker = self.getBroker()
                cash = broker.getCash() * .95

                # 持ち金の98%で売買する

                if date in last_days_of_month and close > self.ma[-1]:
                    quantity = cash / close
                    self.info(f"buying at {close}, which is above {self.ma[-1]}")
                    self.position = self.enterLong(self.instrument, quantity)

            elif close < self.ma[-1] and self.position is not None:
                self.info(f"selling at {close},which is bellow {self.ma[-1]}")
                self.position.exitMarket()
                self.position = None


# load the bar feed from the csv file
feed = yahoofeed.Feed()
feed.addBarsFromCSV("spy", "csv/spy.csv")

# strategy = BuyAndHoldStrategy(feed, "spy")
strategy = MovingAverageStrategy(feed, "spy")

returnsAnalyzer = returns.Returns()
tradesAnalyzer = trades.Trades()
drawDownAnalyzer = drawdown.DrawDown()

strategy.attachAnalyzer(returnsAnalyzer)
strategy.attachAnalyzer(tradesAnalyzer)
strategy.attachAnalyzer(drawDownAnalyzer)

plt = plotter.StrategyPlotter(strategy)
plt.getInstrumentSubplot("spy").addDataSeries("200 day", strategy.ma)

strategy.run()

plt.plot()

print("Final portfolio value: $%.2f" % strategy.getResult())
print("Cumulative returns: $%.2f %%" % (returnsAnalyzer.getCumulativeReturns()[-1] * 100))
print("Max. drawdown duration: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
print("Longest drawdown duration: %s " % (drawDownAnalyzer.getLongestDrawDownDuration()))

print("")
print("Total trades: %d" % (tradesAnalyzer.getCount()))
if tradesAnalyzer.getCount() > 0:
    profits = tradesAnalyzer.getAll()
    print("Avg.profit:$%2.f" % (profits.mean()))
    print("Profits std. dev.: $%2.f" % (profits.std()))
    print("Max. profit:$%2.f" % (profits.min()))
    print("Min. profit:$%2.f" % (profits.max()))
    returns = tradesAnalyzer.getAllReturns()
    print("Avg. return: $%2.f" % (returns.mean() * 100))
    print("Returns std. dev.: $%2.f" % (returns.std() * 100))
    print("Max. return:$%2.f" % (returns.min() * 100))
    print("Min. return:$%2.f" % (returns.max() * 100))


print("")
print("Unprofitable trades: %d" % (tradesAnalyzer.getUnprofitableCount()))
if tradesAnalyzer.getUnprofitableCount() > 0:
    losses = tradesAnalyzer.getLosses()
    print("Avg. loss: $%2.f" % (losses.mean()))
    print("Losses std. dev.: $%2.f" % (losses.std()))
    print("Max. loss:$%2.f" % (losses.min()))
    print("Min. loss:$%2.f" % (losses.max()))
    returns = tradesAnalyzer.getNegativeReturns()
    print("Avg. return: $%2.f" % (returns.mean() * 100))
    print("Returns std. dev.: $%2.f" % (returns.std() * 100))
    print("Max. return:$%2.f" % (returns.min() * 100))
    print("Min. return:$%2.f" % (returns.max() * 100))
