# StockSense
## Stock Price Prediction with Indicators and Backtesting

This application uses historical stock price data along with technical indicators to predict future stock price movements. It integrates both **serial and parallel backtesting** using **multiprocessing** and **OpenMP** to optimize trading strategies, enhance decision-making, and improve workflow efficiency.

---

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Indicators Used](#indicators-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Backtesting](#backtesting)
- [Results & Visualization](#results--visualization)
- [AMD uProf Profiler](#amd-uprof-profiler)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

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

