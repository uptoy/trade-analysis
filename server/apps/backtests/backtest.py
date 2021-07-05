from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed


class BuyAndHoldStrategy(strategy.BacktestingStrategy):

    def __init__(self, feed, instrument):
        super(BuyAndHoldStrategy, self).__init__(feed)
        self.instrument = instrument
        self.setUseAdjustedValues(True)
        self.position = None

    def onEnterOk(self, position):
        self.info(f"{position.getEntryOrder().getExecutionInfo()}")
        # 2000-01-04 00:00:00 strategy [INFO] 2000-01-04 00:00:00 - Price: 96.22866296512284 - Amount: 6875 - Fee: 0

    def onBars(self, bars):
        bar = bars[self.instrument]
        # self.info(bar.getClose())  # ログを記録

        if self.position is None:
            close = bar.getClose()  # 終値
            broker = self.getBroker()
            cash = broker.getCash()
            print(cash)  # 初期所持金1000000

            quantity = cash / close  # 株保有数
            self.position = self.enterLong(self.instrument, quantity)


feed = yahoofeed.Feed()
feed.addBarsFromCSV("spy", "csv/spy.csv")

strategy = BuyAndHoldStrategy(feed, "spy")
strategy.run()
# 2020-01-01 00:00:00 strategy [INFO] 終値

portfolio_value1 = strategy.getBroker().getEquity()  # 運用結果
portfolio_value2 = strategy.getBroker().getEquity() + strategy.getBroker().getCash()  # 運用結果+残高(配当？)
#print(portfolio_value1)  # 2242191.368714979$
#print(portfolio_value2)  # 2565528.781619411

#test