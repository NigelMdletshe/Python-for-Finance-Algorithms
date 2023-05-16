 #backtesting Custom indicators
# run the command below
#pip3 backtesting pandas pandas_ta
#create a virtual env

from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import numpy as np

GOOG["Signal"] = np.random.randinit(-1,2,len(GOOG))


print(GOOG)
class SignalStrategy(Strategy):
    def init(self):
        pass


    def next(self):
        print(self.data.Close[-1])
        print(len(self.data.Close))
        current_signal = self.data.Signal[-1]

        if current_signal == 1:
            if not self.position:
                self.buy()
            elif current_signal == -1:
                if self.position:
                    self.position.close()

    

bt = Backtest(GOOG, SignalStrategy, cash = 10_000)

stats = bt.run()
bt.plot()
# First part to import signals and compare them to random entries end here.

