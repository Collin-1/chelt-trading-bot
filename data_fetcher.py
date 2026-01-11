import ccxt
import pandas as pd
import config

class DataFetcher:
    def __init__(self):
        # We use Binance as an example
        self.exchange = ccxt.binance({
            'apiKey': config.API_KEY,
            'secret': config.API_SECRET
        })

    def get_historical_data(self, limit=100):
        """Fetches OHLCV data and returns a Pandas DataFrame."""
        try:
            bars = self.exchange.fetch_ohlcv(config.SYMBOL, config.TIMEFRAME, limit=limit)
            df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None