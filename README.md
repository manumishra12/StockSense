# StockSense 💹
## Stock Price Prediction with Indicators and Backtesting

This application uses historical stock price data along with technical indicators to predict future stock price movements. It integrates both **serial and parallel backtesting** using **multiprocessing** and **OpenMP** to optimize trading strategies, enhance decision-making, and improve workflow efficiency.


![Prediction in Action](https://github.com/manumishra12/StockSense/blob/main/Assets/demo.gif)

## 📖 Introduction

This project uses **technical indicators** like **MACD**, **RSI**, and **Crossover** to predict stock prices. The application evaluates trading strategies through **serial and parallel backtesting**, using **multiprocessing** and **OpenMP** to speed up computation. It also visualizes the results, showing stock prices, indicators, and buy/sell signals.

---

## ✨ Features

- **Stock Price Prediction**: Predicts future stock movements based on historical prices and technical indicators.
- **Technical Indicators**: 
  - **MACD** (Moving Average Convergence Divergence)
  - **RSI** (Relative Strength Index)
  - **Crossover** (Moving Average Crossovers)
- **Backtesting**: Run both serial and parallel backtests on strategies using multiprocessing and OpenMP.
- **Optimization**: Speed up backtesting by using parallelization for faster results.
- **Visualization**: Plots stock price along with technical indicators and buy/sell signals.

---

## 📊 Indicators Used

- **Close Price**: The daily closing stock price.
- **MACD**: Used to identify the strength and direction of a trend.
- **Crossover**: Signals generated when short-term moving averages cross above or below long-term moving averages.
- **RSI**: Measures the speed and change of price movements to identify overbought or oversold conditions.
- **Combined Indicator Plot**: A plot displaying all indicators combined for better analysis.

---

## ⚙️ Requirements

- Python 3.8+
- `pandas`
- `numpy`
- `matplotlib`
- `yfinance` (for fetching stock data)
- `mplfinance`
- `multiprocessing`
- `OpenMP` (for parallel processing)

---

## 💻 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/username/stock-price-prediction.git
cd stock-price-prediction
```

### 2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
```bash
.\venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Fetch Stock Data
The application uses yfinance to download historical stock data. To fetch data for a specific stock, run the following:

```bash
import yfinance as yf
stock_data = yf.download('AAPL', start='2010-01-01', end='2024-01-01')
```

### 2. Run Prediction and Backtesting
To run the prediction and backtest trading strategies:

```bash
python stock_prediction.py
```

### 3. View Results
The application generates plots showing:

 - Stock's closing price
 - Technical indicators like MACD, RSI, and Crossover
 - Buy/Sell signals based on moving average crossovers


## 🛠️ Backtesting

Backtesting evaluates trading strategies using historical stock data. This application supports both **serial** and **parallel backtesting**:

- **Serial Backtesting**: This mode runs the backtesting sequentially. It's useful for smaller datasets or when you want to perform quick tests on different strategies.
  
- **Parallel Backtesting**: This mode leverages **multiprocessing** and **OpenMP** to speed up the execution by distributing the backtesting process across multiple cores. This is ideal for larger datasets or more intensive analysis, reducing computation time and improving performance.

Both approaches allow for the evaluation of different strategies in a realistic, historical context.

---

## 📈 Results & Visualization

The application provides visual insights into stock price predictions along with key technical indicators. These visualizations help evaluate the stock's historical performance and potential future movements.

- **Close Price**: Displays the stock's historical closing prices over time.
  
- **MACD**: The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator used to identify changes in the strength, direction, and momentum of a stock's price. The plot will show the MACD line along with its signal line.
  
- **RSI**: The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It indicates overbought or oversold conditions of the stock.
  
- **Crossover**: Moving average crossovers signal potential buy or sell points when a short-term moving average crosses above or below a long-term moving average.

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R1.png)

---

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R2.png)

---

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R3.png)

---

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R4.png)


### Example Output

- **Stock Price vs Predicted Prices**: A plot comparing the actual stock prices with predicted prices, allowing for a visual comparison of forecast accuracy.
  
- **MACD and Crossover**: A plot showing the MACD indicator with buy/sell signals based on moving average crossovers.
  
- **RSI**: A plot of the RSI showing overbought and oversold conditions, helping you identify potential entry or exit points.

These plots provide a comprehensive view of how well the trading strategy aligns with market conditions, making it easier to assess the effectiveness of different indicators and strategies.

```bash
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas_ta as ta

# Example: Fetch Stock Data
stock_data = yf.download('AAPL', start='2010-01-01', end='2024-01-01')

# Add MACD and RSI to the dataframe
stock_data['MACD'] = ta.macd(stock_data['Close'])['MACD']
stock_data['RSI'] = ta.rsi(stock_data['Close'], length=14)

# Plot Close Price
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.title('AAPL Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

# Plot MACD
plt.figure(figsize=(10, 6))
plt.plot(stock_data['MACD'], label='MACD', color='blue')
plt.title('MACD Indicator')
plt.xlabel('Date')
plt.ylabel('MACD Value')
plt.legend(loc='upper left')
plt.show()

# Plot RSI
plt.figure(figsize=(10, 6))
plt.plot(stock_data['RSI'], label='RSI', color='green')
plt.title('RSI Indicator')
plt.xlabel('Date')
plt.ylabel('RSI Value')
plt.legend(loc='upper left')
plt.show()

# Example: Moving Average Crossover
short_window = 40
long_window = 100

stock_data['SMA40'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
stock_data['SMA100'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()

# Plot Moving Average Crossover
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA40'], label='40-Day SMA', color='red')
plt.plot(stock_data['SMA100'], label='100-Day SMA', color='orange')
plt.title('Moving Average Crossover')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

```

## 🔧 AMD uProf Profiler

To monitor the performance of your stock price prediction and backtesting script, you can use the **AMD uProf Profiler**, which provides detailed insights into your script's execution, helping you optimize performance.


![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R5.png)

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R6.png)

![Results](https://github.com/manumishra12/StockSense/blob/main/Assets/R7.png)


---

### Steps to Profile with AMD uProf:

1. **Install AMD uProf Profiler**:
   - Download AMD uProf from the official [AMD Developer Tools](https://developer.amd.com/tools-and-sdks/).
   - Follow the installation instructions based on your operating system (Linux or Windows).

2. **Run the Script with AMD uProf**:
   To monitor the execution of your script, use the following command. This will start profiling the script `stock_prediction.py` with AMD uProf:

   ```bash
   amduprof run python stock_prediction.py
   AMDuProfCLI collect -o C:\Users\conne\Desktop\sorting\output C:\Users\conne\AppData\Local\Programs\Python\Python312\python.exe C:\Users\conne\Desktop\sorting\Stock.py
   ```
3. **Analyze the Results**:
   After running the script, use AMD uProf to analyze the performance metrics, identify bottlenecks, and optimize the workflow. 

---

## 🌟 Acknowledgments

- yfinance: For fetching historical stock data.
- TA-Lib: For technical indicators used in the application.
- multiprocessing & OpenMP: For parallel backtesting and efficient computation.
- AMD uProf: For profiling and performance optimization.
