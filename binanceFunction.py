from binance import Client
from binanceKey import apiKey,secKey
import pandas as pd
import ta
import numpy as np

client = Client(apiKey,secKey)
# prices = client.get_all_tickers()
# print(prices)


def getBinanceData(symbol,interval,lookback):
    frame=pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + ' min ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame=frame.astype(float)
    return frame

#df=getminutedata('BTCUSDT', '1m', '100')


def applytechnicals(df):
    df['%K'] = ta.momentum.stoch(df.High,df.Low,df.Close,window=14,smooth_window=3)
    df['%D'] = df['%K'].rolling(3).mean()
    df['rsi'] = ta.momentum.rsi(df.Close, window=14)
    df['macd'] = ta.trend.macd_diff(df.Close)
    df.dropna(inplace = True)


class Signals:
    
    def __init__(self,df,lags):
        self.df = df
        self.lags =lags
        
    
    def gettriger(self):
        dfx = pd.DataFrame()
        for i in range(self.lags+1):
            mask=(self.df['%K'].shift(i)<20) & (self.df['%D'].shift(i)<20)
            dfx = pd.concat([mask],ignore_index=True)
        return dfx.sum(axis=0)
                
    
    def decide(self):#buying trigger return 1 if trigger and 0 if not
        self.df['trigger'] = np.where(self.gettriger(),1,0)
        self.df['Buy'] = np.where((self.df.trigger)
                                  &(self.df['%K'].between(20,80))
                                  &(self.df['%D'].between(20,80))
                                  &(self.df.rsi > 50)
                                  &(self.df.macd>0),1,0)
        


