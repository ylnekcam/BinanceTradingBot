from strategy import taStrategy
import time
import json

def getPathFromJson(jsonpath):

  with open(jsonpath, 'r') as f:
    pathDict = json.load(f)
    return pathDict

data=getPathFromJson('TradeData.json')    
while True:
    #strategy(pair,buylookback,selllookback,qty,target,stoploss,open_position=False)
    taStrategy(data.get("pair"),data.get("buylookback"),data.get("selllookback"),data.get("qty"),data.get("targetpercent"),data.get("stoppercent"))
