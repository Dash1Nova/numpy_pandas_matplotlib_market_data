import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


col_up = '#007560'
col_down = '#BD1414'


def generateData(days, start_price, seed):

    np.random.seed(seed)
    periods = days * 1440

    price_changes = np.random.normal(loc = 0, scale = 0.05, size = periods)
    prices = start_price + np.cumsum(price_changes)

    volume = np.random.randint(1, 5000, size = periods)

    time_index = pd.date_range(start = "2026-02-03", periods = periods, freq = "min")
    df_raw = pd.DataFrame({"Price": prices, "Volume": volume}, index = time_index)

    ohlcv = df_raw["Price"].resample("15min").ohlc()
    ohlcv["Volume"] = df_raw["Volume"].resample("15min").sum()

    ohlcv = ohlcv.reset_index()
    ohlcv.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    return ohlcv


def visualizeData(ohlcv):

    ohlcv['Date'] = pd.to_datetime(ohlcv['Date'])
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (10, 6), sharex = True, gridspec_kw = {'height_ratios': [3, 1]})

    ohlcv = ohlcv.sort_values('Date')
    time_diff = ohlcv['Date'].diff().dropna().median()
    width = time_diff * 0.8
    width2 = width * 0.15

    up = ohlcv[ohlcv['Close'] >= ohlcv['Open']]
    down = ohlcv[ohlcv['Close'] < ohlcv['Open']]

    ax1.bar(up['Date'], up['Close'] - up['Open'], width, bottom = up['Open'], color = col_up)
    ax1.bar(up['Date'], up['High'] - up['Close'], width2, bottom = up['Close'], color = col_up)
    ax1.bar(up['Date'], up['Low'] - up['Open'], width2, bottom = up['Open'], color = col_up)
    ax2.bar(up['Date'], up['Volume'], width, color = col_up)

    ax1.bar(down['Date'], down['Close'] - down['Open'], width, bottom = down['Open'], color = col_down)
    ax1.bar(down['Date'], down['High'] - down['Open'], width2, bottom = down['Open'], color = col_down)
    ax1.bar(down['Date'], down['Low'] - down['Close'], width2, bottom = down['Close'], color = col_down)
    ax2.bar(down['Date'], down['Volume'], width, color = col_down)

    ax1.set_title('Generated one day M15 OHLCV data')
    ax1.set_ylabel('Price')
    ax2.set_ylabel('Volume')
    ax1.set_xlabel('Time')
    ax2.set_xlabel('Time')
    ax2.xaxis_date()

    locator = mdates.HourLocator(byhour = [0, 3, 6, 9, 12, 15, 18, 21])
    formatter = mdates.DateFormatter('%H:%M')

    for ax in (ax1, ax2):
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.tick_params(axis = 'x', labelbottom = True)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    generated_data = generateData(1, 1.3655, 42)
    visualizeData(generated_data)