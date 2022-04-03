from binanceKey import apiKey,secKey
from binance import Client
import pandas as pd
import ta
import numpy
import time

client = Client(apiKey,secKey)


def getminutedata(symbol,interval,lookback):
    frame=pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + ' min ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame=frame.astype(float)
    return frame



