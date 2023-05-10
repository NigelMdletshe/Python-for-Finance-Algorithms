#import packages
import ccxt
import pandas as pd # hleps with storing data
import numpy as np #helps with math
import onecall # connects to exchanges to buy and sell
import time # to implement sleep function
#import file with key and secret

# How to conncet to an exchange
# get API KEYS and secret

#https://phemex.com/account/api-managent
#get API KEY
#get API SECRET
# You can do this for binacne or coinbase whatever

#Connect to the exchange
exchange = ccxt.phemex({
    'enableRateLimit': True,
    'apikey':"715a7a3e-5ff4-467b-92da-f92584f69c69",
    'secret':'Bj7zK3W2xbTrsltexR9aKHX7eev0shPMVcQVOEcdCbs4YTFhMGFkYS1kNTM2LTQ0NDMtYmU4Yi1mMGI5OWQwNzU4Y2Y' # Must be hidden from public
    # save key and secret in a file and import it
})

symbol    = 'uBTCUSD'
pos_size  = 100
timeframe = '15m'
pos_perc  = 0.05 

#make trades
#exchange.create_limit_buy_order()

#set up a sell order
#exchange.create_limit_sell_order()

# see total balance
balance = exchange.fetch_balance()
print(balance)

#if 2 red bars,buy
# sell after 1 green bar

#Having issues installing Vectorbt, inside the env or globally