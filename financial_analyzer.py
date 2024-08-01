import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

def calculate_metrics(data):
    metrics = {}
    metrics['mean_close'] = data['Close'].mean()
    metrics['std_dev_close'] = data['Close'].std()
    metrics['total_volume'] = data['Volume'].sum()
    metrics['volatility'] = data['Close'].pct_change().std() * np.sqrt(252)
    metrics['sharpe_ratio'] = data['Close'].pct_change().mean() / data['Close'].pct_change().std() * np.sqrt(252)
    metrics['max_drawdown'] = (data['Close'] / data['Close'].cummax() - 1).min()
    return metrics

def moving_average(data, window=3):
    return data['Close'].rolling(window=window).mean()

def macd(data):
    short_ema = data['Close'].ewm(span=12, adjust=False).mean()
    long_ema = data['Close'].ewm(span=26, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def bollinger_bands(data, window=20):
    sma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    upper_band = sma + (std * 2)
    lower_band = sma - (std * 2)
    return upper_band, lower_band

def plot_data(data, moving_avg, macd, signal, rsi, upper_band, lower_band):
    fig, axs = plt.subplots(3, figsize=(10, 15))
    
    axs[0].plot(data['Date'], data['Close'], label='Close Price')
    axs[0].plot(data['Date'], moving_avg, label='Moving Average', linestyle='--')
    axs[0].set_title('Stock Price and Moving Average')
    axs[0].legend()
    
    axs[1].plot(data['Date'], macd, label='MACD')
    axs[1].plot(data['Date'], signal, label='Signal Line', linestyle='--')
    axs[1].set_title('MACD')
    axs[1].legend()
    
    axs[2].plot(data['Date'], rsi, label='RSI')
    axs[2].axhline(70, color='r', linestyle='--')
    axs[2].axhline(30, color='g', linestyle='--')
    axs[2].set_title('Relative Strength Index (RSI)')
    axs[2].legend()
    
    fig.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Financial Data Analyzer')
    parser.add_argument('--file', type=str, required=True, help='Path to the financial data CSV file')
    parser.add_argument('--window', type=int, default=3, help='Window size for moving average')
    
    args = parser.parse_args()
    
    data = load_data(args.file)
    metrics = calculate_metrics(data)
    
    print("Financial Data Analysis")
    print("------------------------")
    print(f"Mean Close Price: {metrics['mean_close']:.2f}")
    print(f"Standard Deviation of Close Price: {metrics['std_dev_close']:.2f}")
    print(f"Total Volume: {metrics['total_volume']}")
    print(f"Volatility: {metrics['volatility']:.2f}")
    print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
    print(f"Max Drawdown: {metrics['max_drawdown']:.2%}")
    
    moving_avg = moving_average(data, args.window)
    macd_line, signal_line = macd(data)
    rsi_line = rsi(data)
    upper_band, lower_band = bollinger_bands(data)
    
    plot_data(data, moving_avg, macd_line, signal_line, rsi_line, upper_band, lower_band)

if __name__ == '__main__':
    main()
