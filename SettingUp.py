#import packages
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
onecall = onecall.phemex(
    key="715a7a3e-5ff4-467b-92da-f92584f69c69",
    secret='Bj7zK3W2xbTrsltexR9aKHX7eev0shPMVcQVOEcdCbs4YTFhMGFkYS1kNTM2LTQ0NDMtYmU4Yi1mMGI5OWQwNzU4Y2Y' # Must be hidden from public
    # save key and secret in a file and import it
)
#check our balance
bal = onecall.get_balance()
#jump to start: Command + arrow left
#jump to end: command + arrow right
print(bal)
#get our positions
pos = onecall.get_positions('USD')
print(pos)
#get order book data
ob = onecall.get_orderbook('ETHUSD',True)
#print(ob)
#get historical data
data = onecall.get_data('ETHUSH',onecall.MINUTE_5, is_dataframe= True)
print(data)
#Buy and Sell variables
buy = onecall.BUY_SIDE
sell = onecall.SELL_SIDE
size = 1
#BUY ORDER
onecall.market_order('ETHUSD',buy,size)
time.sleep(4)
#SELL order
onecall.market_order('ETHUSD',sell,size)

