# Financial Data Analysis

## Overview

This repository contains an extensive financial dataset covering multiple years of daily trading data. The dataset includes daily open, high, low, close, and volume figures for a fictional stock.

## Dataset

The dataset (`financial_data.csv`) contains the following columns:
- **Date**: The trading date
- **Open**: The opening price of the stock
- **High**: The highest price of the stock during the trading day
- **Low**: The lowest price of the stock during the trading day
- **Close**: The closing price of the stock
- **Volume**: The number of shares traded

## Example Usage

Below is an example of how you can load and analyze the dataset using Python:

```python
import pandas as pd

# Load the dataset
data = pd.read_csv('financial_data.csv')

# Display the first few rows
print(data.head())

# Calculate basic statistics
print(data.describe())

# Plot the closing prices over time
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Closing Prices Over Time')
plt.legend()
plt.show()
```
## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/brettadams0/financial-data-analysis.git
```
## Navigate to the project directory:

```bash
cd financial-data-analysis
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
