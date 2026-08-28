import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


col_up = '#007560'
col_down = '#BD1414'


def loadDataTick(path):

    data = pd.read_csv(path, header = None, names = ['Date', 'Bid', 'Ask', 'Volume'])
    data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d %H%M%S%f')
    data = data[(data['Date'] >= '2026-07-15 12:00:00') & (data['Date'] < '2026-07-15 13:00:00')]

    return data


def loadData1M1D(path):

    data = pd.read_csv(path, header = None, names = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'], sep=r'\s+')
    data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format = '%Y-%m-%d %H:%M')

    if path == 'data/GBP-USD_1M.csv':
        data = data[(data['Date'] >= '2026-07-15 00:00:00') & (data['Date'] < '2026-07-16 00:00:00')]
    elif path == 'data/GBP-USD_daily.csv':
        data = data[(data['Date'] >= '2020-01-01 00:00:00') & (data['Date'] < '2026-01-01 00:00:00')]

    return data


def visualizeTick(data, path):

    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Bid'], color = col_up, label = 'Bid')
    plt.plot(data['Date'], data['Ask'], color = col_down, label = 'Ask')
    plt.xlabel('Time')
    plt.ylabel('Price')
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute = [0, 10, 20, 30, 40, 50], interval = 1))
    plt.legend()
    plt.title('Forex Tick Data 2026-07-15 12:00-13:00')
    plt.grid()
    plt.show()


def visualize1M1D(data, path):

    if path == 'data/GBP-USD_1M.csv':
        title = 'Forex OHLC prices 2026-07-15'
        is_1m = True
    elif path == 'data/GBP-USD_daily.csv':
        title = 'Forex OHLC prices 2020-2025'
        is_1m = False

    data = data.sort_values('Date')
    time_diff = data['Date'].diff().dropna().median()
    width = time_diff * 0.8
    width2 = width * 0.15

    up = data[data['Close'] >= data['Open']]
    down = data[data['Close'] < data['Open']]

    plt.figure(figsize = (10, 6))

    plt.bar(up['Date'], up['Close'] - up['Open'], width, bottom = up['Open'], color = col_up)
    plt.bar(up['Date'], up['High'] - up['Close'], width2, bottom = up['Close'], color = col_up)
    plt.bar(up['Date'], up['Low'] - up['Open'], width2, bottom = up['Open'], color = col_up)

    plt.bar(down['Date'], down['Close'] - down['Open'], width, bottom = down['Open'], color = col_down)
    plt.bar(down['Date'], down['High'] - down['Open'], width2, bottom = down['Open'], color = col_down)
    plt.bar(down['Date'], down['Low'] - down['Close'], width2, bottom = down['Close'], color = col_down)

    ax = plt.gca()
    if is_1m:
        locator = mdates.HourLocator(byhour = [0, 3, 6, 9, 12, 15, 18, 21])
        formatter = mdates.DateFormatter('%H:%M')
    else:
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)

    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    plt.xticks()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title(title)
    plt.show()


if __name__ == '__main__':

    tick_data = loadDataTick('data/GBP-USD_1Tick.csv')
    minute_data = loadData1M1D('data/GBP-USD_1M.csv')
    daily_data = loadData1M1D('data/GBP-USD_daily.csv')
    visualizeTick(tick_data, 'data/GBP-USD_1Tick.csv')
    visualize1M1D(minute_data, 'data/GBP-USD_1M.csv')
    visualize1M1D(daily_data, 'data/GBP-USD_daily.csv')