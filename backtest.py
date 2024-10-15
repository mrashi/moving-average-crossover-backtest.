# Main script for strategy and backtesting


---

#### 4. **backtest.py**

This file will contain the actual code to implement the strategy and backtest.

```python
import backtrader as bt
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

class MovingAverageCrossover(bt.Strategy):
    params = (('short_period', 50), ('long_period', 200))

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if not self.position:  # Not in the market
            if self.short_ma > self.long_ma:
                self.buy()  # Buy signal
        elif self.short_ma < self.long_ma:
            self.sell()  # Sell signal

# Initialize Cerebro engine
cerebro = bt.Cerebro()

# Add strategy to Cerebro
cerebro.addstrategy(MovingAverageCrossover)

# Download data using Yahoo Finance
data = bt.feeds.PandasData(dataname=yf.download('SPY', start='2020-01-01', end='2023-01-01'))

# Add data to Cerebro
cerebro.adddata(data)

# Set initial capital
cerebro.broker.setcash(10000)

# Run backtest
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the results
cerebro.plot()
