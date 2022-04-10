from binanceFunction import getMinuteData,applytechnicals,Signals
from filefunction import getPathFromJson
from binance import Client
import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')
pair='XMRUSDT'
dataKey=getPathFromJson('Bkey.json')
client = Client(dataKey.get("apiKey"),dataKey.get("secKey"))
df = getMinuteData(client,pair,'1m','200')
applytechnicals(df)
inst = Signals(df,50)
inst.decide()
df.to_sql('TA_'+pair, engine, if_exists = 'append',index=False)
d=df[df.Buy==1]
d.to_sql('TA_BUY'+pair, engine, if_exists = 'append',index=False)

