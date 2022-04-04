# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:44:45 2022

@author: kaili
"""
from binanceKey import apiKey,secKey
import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager,AsyncClient
import asyncio


client = Client(apiKey,secKey)

bm = BinanceSocketManager(client, user_timeout=60)
ts = bm.trade_socket('BNBBTC')
# enter the context manager
await ts.__aenter__()
# receive a message
msg = await ts.recv()
print(msg)
# exit the context manager
await ts.__aexit__(None, None, None)