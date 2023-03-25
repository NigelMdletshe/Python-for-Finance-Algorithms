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
print(bal)

### Inputs###########################################
size         =  5 # total size we want to buy buy sell
size_1       = size*.2 # 20%
size_2_3     = size*.4 # 40%
symbol       = 'uBTCUSD'
perc_from_lh = .35
close_seocnds= 60*47
max_lh       = 800
timeframe    = '5m'
num_bars     = 180
max_risk     = 1000  #$1000
sl_perc      = 0.1
exit_perc    = 0.004 # 8/20 - moved from .002 to .004
max_tr       = 550
quartile     = 0.33
time_limit   = 120 # changed 8/20 from 60 mins to 2 hours
sleep        = 30
#################################################

def kill_switch():
    openposi = open_positions()[1] #this returns T/F for open ....
    long     = open_positions()[3] #this sets long to T/F


    print('Kill Switch Activated...going to loop til limit...')
    print(f' open position is set to: {openposi} if true ...')

    btc_kill_size = open_positions()[2] # this gets the open pos...
    btc_kill_size = int(btc_kill_size) # converts valure to int

    while openposi == True:
        print('start kill switch loop again til limit fill ...')
        temp_df = pd.DataFrame()
        print('just made a new temp_df for the kill switch..')




