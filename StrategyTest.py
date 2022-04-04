# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:50:52 2022

@author: kaili
"""
from binanceFunction import getBinanceData,applytechnicals,Signals
import time
import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')

def strategy(pair,qty,open_position=False):
    df = getBinanceData(pair,'1m','100')
    applytechnicals(df)
    inst = Signals(df,25)
    inst.decide()
    if df.Buy.iloc[-1]:
        df.to_sql('ADAUSDT', engine, if_exists = 'append',index=False)
        d=df.iloc[[-1]]
        d.to_sql('Buy', engine, if_exists = 'append',index=False)
        buyprice=float(d.Close.iloc[-1])
        print(f'Sybol: ADAUSDT,BUY {qty} Price:{df.Close[-1]}')
        open_position = True

    while open_position:
        time.sleep(0.5)
        df = getBinanceData('ADAUSDT', '1m', '2')   
        if df.Close[-1] <= buyprice * 0.995 or df.Close [-1] >= 1.005 * buyprice:
            print(f'Sybol: ADAUSDT,Sell Price:{df.Close[-1]}')
            break
    
print('Test Run')
while True:
    strategy('ADAUSDT',2)
    time.sleep(0.5)
    