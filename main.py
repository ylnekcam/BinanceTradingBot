from binanceFunction import getBinanceData,applytechnicals,Signals
import time

def strategy(pair,qty,open_position=False):
    df = getBinanceData(pair,'1m','100')
    applytechnicals(df)
    inst = Signals(df,25)
    inst.decide()
    print(f'current Close is ' +str(df.Close.iloc[-1]))
    if df.Buy.iloc[-1]:
        #create an order
        #order = client.create_order(symbol=pair,side='BUY',type='MARKET',quantity=qty)
        #print(order)
        #buyprice=float(order['fills'][0]['price])
        
        
        #sample only for test uncomment the order if you want to use the app
        print(buyprice=float(df.BUY))
        testorder = f'Sybol: {pair},side:BUY,type=MARKET,quantity={qty}'
        print(testorder)
        open_position = True
     
    
    while open_position:
        time.sleep(0.5)
        df = getBinanceData(pair, '1m', '2')
        # print(f'current Close ' + str(df.Close.iloc[-1]))
        # print(f'current Target ' + str(buyprice * 1.005))
        # print(f'current Stop is ' + str(buyprice * 0.995))
        #if df.Close[-1] <= buyprice * 0.995 or df.Close [-1] >= 1.005 * buyprice:
        #     order = client.create_order(symbol=pair,side='SELL',type='MARKET',quantity=qty)
        #     print(order)
                #for test only 
        print(f'Sybol: {pair},side:SELL,type=MARKET,quantity={qty}')
        break
    

while True:
    strategy('ADAUSDT',2)
    time.sleep(0.5)
    