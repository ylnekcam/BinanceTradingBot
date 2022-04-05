from StrategyTest import taStrategy
import json

def getPathFromJson(jsonpath):

  with open(jsonpath, 'r') as f:
    pathDict = json.load(f)
    return pathDict

data=getPathFromJson('TradeData.json')    
print(data)
print(f'Bot Start')
while True:
    #taStrategy("ADAUSDT","100","2",2,1.005,0.995)
    taStrategy(data.get("pair"),data.get("buylookback"),data.get("qty"),data.get("targetpercent"),data.get("stoppercent"))