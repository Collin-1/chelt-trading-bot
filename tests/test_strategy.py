import unittest
import pandas as pd
import sys
import os

# Add parent directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategy import MovingAverageStrategy

class TestStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = MovingAverageStrategy(short_window=2, long_window=5)

    def test_buy_signal(self):
        # Create fake data where a crossover happens
        data = {
            'close': [100, 100, 100, 100, 90, 120]
        }
        df = pd.DataFrame(data)
        
        # Run analysis
        signal = self.strategy.analyze(df)
        
        # We expect a BUY because price shot up, pulling short avg above long avg
        self.assertEqual(signal, 'BUY')

    def test_no_signal(self):
        # Flat data, lines never cross
        data = {'close': [100, 100, 100, 100, 100, 100]}
        df = pd.DataFrame(data)
        self.assertEqual(self.strategy.analyze(df), None)

if __name__ == '__main__':
    unittest.main()