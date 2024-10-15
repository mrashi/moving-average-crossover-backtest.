# Moving Average Crossover Strategy

A simple moving average crossover strategy for backtesting using Python and Backtrader.
This repository contains a simple **Moving Average Crossover Strategy** for backtesting with **Python** and **Backtrader**. The strategy uses short-term and long-term moving averages to generate buy/sell signals, allowing traders to capture trend-following opportunities.

## Strategy Overview

- **Short-term Moving Average**: Represents short-term price trends (e.g., 50 days).
- **Long-term Moving Average**: Represents long-term price trends (e.g., 200 days).
- **Buy Signal**: When the short-term MA crosses above the long-term MA (bullish signal).
- **Sell Signal**: When the short-term MA crosses below the long-term MA (bearish signal).

## Key Metrics
- **Sharpe Ratio**: Risk-adjusted return measure.
- **Max Drawdown**: Maximum potential loss during the trading period.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/moving-average-crossover-backtest.git
cd moving-average-crossover-backtest

#2. Install Required Libraries
Make sure you have the following Python packages installed:
pip install yfinance backtrader matplotlib

#3. Run the Strategy
You can backtest the strategy by running the Python script:
python backtest.py

#4. Visualization
You can visualize the results with a plot of the moving averages and buy/sell signals.

Code Overview


