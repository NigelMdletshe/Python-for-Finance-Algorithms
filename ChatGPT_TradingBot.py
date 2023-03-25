'''
When bitcoin breaks out of consolidation
to the upside, entera a order to go long

when bitcoin breaks out of consolidation to the downside, enter an order
to go short. Close that  order when it makes a 6% gain or a a 3% loss 

'''
import ccxt
import pandas as pd
import time

# Connect to the Phemex exchange

exchange = ccxt.phemex({
    'enableRateLimit': True,
    'apiKey'         :'715a7a3e-5ff4-467b-92da-f92584f69c69',
    'secret'         :'Bj7zK3W2xbTrsltexR9aKHX7eev0shPMVcQVOEcdCbs4YTFhMGFkYS1kNTM2LTQ0NDMtYmU4Yi1mMGI5OWQwNzU4Y2Y'
})

# Set the current trading pair and fetch the current price
symbol = 'uBTCUSD'
price  = exchange.fetch_ticker(symbol)['last']
print(price)

# Set the profit and loss thresholds for cclosing an order
profit_threshold = 0.06
loss_threshold   = 0.03
size             = 1

def calculate_consolidation_price():
    '''
    This function looks at the past 24 hours and gets consolidation and then returns consolidation price ONLY if in consol,
    if not it retrns None

    '''
    
    #Fetch the past 24 hours of candlestick data for the pair
    candles = exchange.fetch_ohlcv(symbol,'1h')[-24:]

    #calculate the range of prices over the past 24 hours
    high = max(candle[2] for candle in candles)
    low  = min(candle[3] for candle in candles)
    range= high - low

    print(f'this is the high {high} low {low} range {range}')

    #if the range is than 2%, return the average price as the consolodittion price
    if range / low < 0.02:
        return sum(candle[4] for candle in candles) / len(candles)
        #Otherwise, return none to indicate that the market is not consolidated
    else:
        return None

while True:
    # Calculate the consoloditation price
    consolidation_price = calculate_consolidation_price()
    #if there is a consolidation price move on
    if consolidation_price:

        # Fetch the current price and see if it has broken out of consilidation
        price = exchange.fetch_ticker(symbol)['last']
        print(f'This is the symbol: {symbol} and price:{price}')
        
        if price > consolidation_price:
            #if the price has broken out to the upside, enter a long order
            order = exchange.create_order(symbol,'limit','buy',size,price)

            while True:
            #Check the current price and close the order if the profit or loss threshold has been reached
                price = exchange.fetch_ticker(symbol)['last']
                profit = (price - order['price']) / order['price']
                if profit >= profit_threshold or profit <= -loss_threshold:
                    exchange.cancel_order(order['id'])
                    break
                time.sleep(30) #wait 30s before checking price again
        elif price < consolidation_price:
        #if price has broken out to the downside, enter a short order
            order = exchange.create_order(symbol,'limit','sell',size,price)
            while True:
                # Check the current price and close the oder if the profit or loss threshold have been reached
                price = exchange.fetch_ticker(symbol)['last']
                profit = ( order['price']- price) / order['price']
                if profit >= profit_threshold or profit <= -loss_threshold:
                    exchange.cancel_order(order['id'])
                    break
                time.sleep(30) #wait 30s before checking price again

time.sleep(30) #wait 30s before checking price again


# ended on 35min