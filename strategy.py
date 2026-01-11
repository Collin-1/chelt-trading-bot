import pandas as pd

class MovingAverageStrategy:
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def analyze(self, df):
        """
        Input: Pandas DataFrame
        Output: 'BUY', 'SELL', or None
        """
        # Create copies to avoid SettingWithCopy warnings
        df = df.copy()
        
        # Calculate indicators
        df['short_mavg'] = df['close'].rolling(window=self.short_window).mean()
        df['long_mavg'] = df['close'].rolling(window=self.long_window).mean()

        # Get last two rows
        current = df.iloc[-1]
        previous = df.iloc[-2]

        # Golden Cross (Short crosses above Long)
        if previous['short_mavg'] < previous['long_mavg'] and current['short_mavg'] > current['long_mavg']:
            return 'BUY'
        
        # Death Cross (Short crosses below Long)
        elif previous['short_mavg'] > previous['long_mavg'] and current['short_mavg'] < current['long_mavg']:
            return 'SELL'
            
        return None