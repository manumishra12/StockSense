import matplotlib.pyplot as plt
import yfinance as yf
import multiprocessing
import pandas as pd
import time

# Fetch stock data
def fetch_data(ticker, start_date="2020-01-01", end_date="2024-01-01"):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

# Moving Average Crossover Strategy
def moving_average_crossover(data, short_window=50, long_window=200):
    data['short_ma'] = data['Close'].rolling(window=short_window).mean()
    data['long_ma'] = data['Close'].rolling(window=long_window).mean()
    data['mac_signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'mac_signal'] = 1
    data.loc[data['short_ma'] <= data['long_ma'], 'mac_signal'] = -1
    data['mac_buy_sell'] = data['mac_signal'].diff()
    return data

# MACD Strategy
def macd_strategy(data):
    data['ema_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['ema_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['macd'] = data['ema_12'] - data['ema_26']
    data['signal_line'] = data['macd'].ewm(span=9, adjust=False).mean()
    data['macd_signal'] = 0
    data.loc[data['macd'] > data['signal_line'], 'macd_signal'] = 1
    data.loc[data['macd'] <= data['signal_line'], 'macd_signal'] = -1
    data['macd_buy_sell'] = data['macd_signal'].diff()
    return data

# RSI Strategy
def rsi_strategy(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['rsi'] = 100 - (100 / (1 + rs))
    data['rsi_signal'] = 0
    data.loc[data['rsi'] < 30, 'rsi_signal'] = 1  # Buy signal
    data.loc[data['rsi'] > 70, 'rsi_signal'] = -1  # Sell signal
    data['rsi_buy_sell'] = data['rsi_signal'].diff()
    return data

# Combine All Strategies
def apply_strategies(data):
    data = moving_average_crossover(data)
    data = macd_strategy(data)
    data = rsi_strategy(data)
    return data

# Identify Buy/Sell Points for Combined Strategies
def find_combined_buy_sell_points(data):
    buy_points = data[(data['mac_buy_sell'] == 2) | (data['macd_buy_sell'] == 2) | (data['rsi_buy_sell'] == 2)]
    sell_points = data[(data['mac_buy_sell'] == -2) | (data['macd_buy_sell'] == -2) | (data['rsi_buy_sell'] == -2)]
    return buy_points, sell_points

# Plot All Strategies and Combined Signals
def plot_all_strategies(data, buy_points, sell_points, ticker):
    plt.figure(figsize=(16, 10))

    # Plot Close Price
    plt.subplot(3, 1, 1)
    plt.plot(data['Date'], data['Close'], label='Close Price', color='black', lw=1)
    plt.plot(data['Date'], data['short_ma'], label='Short MA (50)', color='blue', linestyle='--')
    plt.plot(data['Date'], data['long_ma'], label='Long MA (200)', color='red', linestyle='--')
    plt.scatter(buy_points['Date'], buy_points['Close'], color='green', marker='^', s=100, label='Buy Signal')
    plt.scatter(sell_points['Date'], sell_points['Close'], color='red', marker='v', s=100, label='Sell Signal')
    plt.title(f"{ticker} - Price and Moving Averages")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()

    # Plot MACD
    plt.subplot(3, 1, 2)
    plt.plot(data['Date'], data['macd'], label='MACD', color='blue')
    plt.plot(data['Date'], data['signal_line'], label='Signal Line', color='red', linestyle='--')
    plt.fill_between(data['Date'], data['macd'] - data['signal_line'], color='gray', alpha=0.3, label='MACD Histogram')
    plt.title('MACD and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.grid()

    # Plot RSI
    plt.subplot(3, 1, 3)
    plt.plot(data['Date'], data['rsi'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

# Backtest Strategy
def backtest_strategy(ticker):
    data = fetch_data(ticker)
    data = apply_strategies(data)
    buy_points, sell_points = find_combined_buy_sell_points(data)
    plot_all_strategies(data, buy_points, sell_points, ticker)
    return data

# Serial Backtesting
def backtest_serial(tickers):
    results = {}
    for ticker in tickers:
        print(f"Backtesting {ticker} in Serial Mode...")
        start = time.time()
        data = backtest_strategy(ticker)
        execution_time = time.time() - start
        results[ticker] = {'execution_time': execution_time}
    return results

# Parallel Backtesting Helper
def run_parallel_backtest(ticker, return_dict):
    print(f"Running backtest for {ticker}...")
    start = time.time()
    data = backtest_strategy(ticker)
    execution_time = time.time() - start
    return_dict[ticker] = {'execution_time': execution_time}
    print(f"Backtest for {ticker} completed.")

# Parallel Backtesting
def backtest_parallel(tickers):
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    processes = []
    for ticker in tickers:
        process = multiprocessing.Process(target=run_parallel_backtest, args=(ticker, return_dict))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return return_dict

# Main Function
if __name__ == "__main__":
    stock_tickers = ['AAPL', 'GOOGL', 'MSFT']  # Add more tickers as needed
    
    # Serial Backtesting
    print("Starting Serial Backtest...")
    start_time = time.time()
    serial_results = backtest_serial(stock_tickers)
    serial_time = time.time() - start_time
    print(f"Total Time for Serial Backtest: {serial_time:.2f} seconds")
    
    # Parallel Backtesting
    print("\nStarting Parallel Backtest...")
    start_time = time.time()
    parallel_results = backtest_parallel(stock_tickers)
    parallel_time = time.time() - start_time
    print(f"Total Time for Parallel Backtest: {parallel_time:.2f} seconds")
    
    # Compare Execution Times
    plt.figure(figsize=(8, 5))
    plt.bar(['Serial', 'Parallel'], [serial_time, parallel_time], color=['blue', 'orange'])
    plt.xlabel('Backtest Mode')
    plt.ylabel('Time (seconds)')
    plt.title('Backtest Time Comparison: Serial vs Parallel')
    plt.show()
