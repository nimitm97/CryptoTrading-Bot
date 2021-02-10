import backtrader as bt
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, timeperiod=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

# fromdate = datetime.datetime.strptime('2020-04-01', '%Y-%m-%d')
# todate = datetime.datetime.strptime('2020-09-10', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='data/niharika_test.csv', dtformat=2, compression=5, timeframe=bt.TimeFrame.Minutes)
# data = bt.feeds.GenericCSVData(dataname='data/2020_15minutes.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()