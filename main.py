from StrategyTest import taStrategy
from filefunction import getPathFromJson
from binance.client import Client

dataKey=getPathFromJson('Bkey.json')
client = Client(dataKey.get("apiKey"),dataKey.get("secKey"))
data=getPathFromJson('TradeData.json')    
print(data)
print(f'Bot Start')

while True:
    #taStrategy("ADAUSDT","100","2",2,1.005,0.995)
    taStrategy(client,data.get("pair"),data.get("lags"),data.get("buylookback"),data.get("qty"),data.get("targetpercent"),data.get("stoppercent"))