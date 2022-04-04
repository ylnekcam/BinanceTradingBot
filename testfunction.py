from binanceFunction import getBinanceData,applytechnicals,Signals
import time
import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')
#while True:
df = getBinanceData('ADAUSDT','1m','100')  
applytechnicals(df)
#df.to_sql('ADAUSDT', engine, if_exists = 'append',index=False)
inst = Signals(df,5)
inst.decide()
print(f'current Close is ' +str(df.Close.iloc[-1]))
print(df.Buy.iloc[-1])
print(df.trigger.iloc[-1])
#d=df[df['Buy']==1]#get all buy==1
#print(d)

open_position=False
bfdf=pd.DataFrame()

if df.Buy.iloc[-1]==0:
    df.to_sql('ADAUSDT', engine, if_exists = 'append',index=False)
    d=df.iloc[[-1]]
    d.to_sql('Buy', engine, if_exists = 'append',index=False)
    buyprice=float(d.Close.iloc[-1])
    print(f'Sybol: ADAUSDT,BUY Price:{df.Close[-1]}')
    open_position = True

while open_position:
    time.sleep(0.5)
    df = getBinanceData('ADAUSDT', '1m', '2')   
    print(f'current Close is ' +str(df.Close.iloc[-1]))
    if df.Close[-1] <= buyprice * 0.995 or df.Close [-1] >= 1.005 * buyprice:
        print(f'Sybol: ADAUSDT,Sell Price:{df.Close[-1]}')
        break