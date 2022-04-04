from binanceFunction import getBinanceData,applytechnicals,Signals
import time
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///BinanceData.db')

def taStrategy(pair,buylookback,selllookback,qty,target,stoploss,open_position=False):
    df = getBinanceData(pair,'1m',buylookback)
    applytechnicals(df)
    inst = Signals(df,25)
    inst.decide()
    print(f'current Close is ' +str(df.Close.iloc[-1]))
    if df.Buy.iloc[-1]:
        #create an order uncomment if you want to use
        # order = createOrder(pair,'BUY','MARKET',qty)
        # print(order)
        df.to_sql('TA_'+pair, engine, if_exists = 'append',index=False)
        d=df.iloc[[-1]]
        d.to_sql('TA_Buy', engine, if_exists = 'append',index=False)
        buyprice=float(d.Close.iloc[-1])
        print(f'Symbol:{pair}, BUY {qty} Price:{df.Close[-1]}')
        open_position = True

    
    while open_position:
        time.sleep(0.5)
        df = getBinanceData(pair, '1m', selllookback)
        print(f'current Close ' + str(df.Close.iloc[-1]))
        print(f'current Target ' + str(buyprice * target))
        print(f'current Stop is ' + str(buyprice * stoploss))
        if df.Close[-1] <= buyprice * 0.995 or df.Close [-1] >= 1.005 * buyprice:
            #uncomment if you want to use
            # order = order = createOrder(pair,'SELL','MARKET',qty)
            # print(order)
            d=df.iloc[[-1]]
            d.to_sql('TA_SELL', engine, if_exists = 'append',index=False)
            print(f'Sybol: {pair},side:SELL,type=MARKET,quantity={qty}')
        break
    

    