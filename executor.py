import ccxt
import config

class Executor:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': config.API_KEY,
            'secret': config.API_SECRET
        })

    def place_order(self, side):
        print(f"Attempting to {side} {config.SYMBOL}...")
        # UNCOMMENT BELOW FOR REAL TRADES
        # order = self.exchange.create_market_order(config.SYMBOL, side, amount=0.001)
        # print(f"Order executed: {order}")
        print("Paper trade successful (Simulated).")