from ntpath import join
from binanceFunction import getMinuteData,applytechnicals,Signals
import time
import json
#import sqlalchemy
from datetime import datetime


#engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')
def getPathFromJson(jsonpath):

  with open(jsonpath, 'r') as f:
    pathDict = json.load(f)
    return pathDict


def writeTxt(path,txt):
    with open(path, 'a') as f:
        return f.writelines(txt +'\n')


def taStrategy(client,pair,buylookback,qty,target,stoploss,open_position=False):
    df = getMinuteData(client,pair,'1m',buylookback)
    applytechnicals(df)
    inst = Signals(df,25)
    inst.decide()
    #print(f'current Close is ' +str(df.Close.iloc[-1]))
    if df.Buy.iloc[-1]:
        #create an order uncomment if you want to use
        # order = createOrder(client,pair,'BUY','MARKET',qty)
        # print(order)
        #df.to_sql('TA_'+pair, engine, if_exists = 'append',index=False)
        #d.to_sql('TA_Buy', engine, if_exists = 'append',index=False)
        buyprice=float(df.Close.iloc[-1])
        t=buyprice * target
        s=buyprice * stoploss
        buysym=f'Symbol:{pair}, QTY:{qty}, Price:{df.Close[-1]}'
        writeTxt('Result.txt',buysym)
        buyres=f'BUYTime:{datetime.now()}, BuyPrice:{str(df.Close.iloc[-1])}, current Target: {str(t)}, current Stop is: {str(s)} '
        writeTxt('Result.txt',buyres)
        print(buyres)
        print(f'Waiting to Sell....Position Open...BuyPrice:{str(df.Close.iloc[-1])} ')
        open_position = True

    
    while open_position:
        time.sleep(0.5)
        df = getMinuteData(client,pair, '1m', '2')
        if df.Close[-1] <= s or df.Close [-1] >= t:
            #uncomment if you want to use
            # order = createOrder(client,pair,'SELL','MARKET',qty)
            # print(order) 
            traderes='loss' if df.Close[-1] <= s else 'win'
            res=f'{traderes}: SELLTime:{datetime.now()}, Symbol: {pair}, side:SELL,Price:{df.Close[-1]},type=MARKET,quantity={qty}'
            writeTxt('Result.txt',res)
            #res.to_sql('TA_SELL', engine, if_exists = 'append',index=False)
            print(res)
            break
    

    