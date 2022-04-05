from binanceFunction import getBinanceData,applytechnicals,Signals
import time
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')

def taStrategy(pair,buylookback,selllookback,qty,target,stoploss,open_position=False):
    df = getBinanceData(pair,'1m',buylookback)
    applytechnicals(df)
    inst = Signals(df,25)
    inst.decide()
    #print(f'current Close is ' +str(df.Close.iloc[-1]))
    if df.Buy.iloc[-1]==0:
        #create an order uncomment if you want to use
        # order = createOrder(pair,'BUY','MARKET',qty)
        # print(order)
        df.to_sql('TA_'+pair, engine, if_exists = 'append',index=False)
        d=df.iloc[[-1]]
        d.to_sql('TA_Buy', engine, if_exists = 'append',index=False)
        buyprice=float(d.Close.iloc[-1])
        t=buyprice * target
        s=buyprice * stoploss
        print(f'Symbol:{pair}, BUY {qty} Price:{df.Close[-1]}')
        print(f'current Close ' + str(df.Close.iloc[-1]))
        print(f'current Target ' + str(t))
        print(f'current Stop is ' + str(s))
        print(f'Waiting to Sell....Position Open... Sell lookback: {selllookback} ')
        open_position = True

    
    while open_position:
        time.sleep(0.5)
        df = getBinanceData(pair, '1m', selllookback)
        if df.Close[-1] <= s or df.Close [-1] >= t:
            #uncomment if you want to use
            # order = order = createOrder(pair,'SELL','MARKET',qty)
            # print(order)
            ds=df.iloc[[-1]]
            ds.to_sql('TA_SELL', engine, if_exists = 'append',index=False)
            print(f'Sybol: {pair}, side:SELL,Price:{df.Close[-1]},type=MARKET,quantity={qty}')
            if df.Close[-1] <= s:
                print('loss')
            else:
                print('win')


            break
    

    