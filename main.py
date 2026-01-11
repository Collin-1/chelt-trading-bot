import time
import logging
import sys
from data_fetcher import DataFetcher
from strategy import MovingAverageStrategy
from executor import Executor

# --- LOGGING SETUP ---
# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 1. File Handler (Saves to file)
file_handler = logging.FileHandler('bot.log')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# 2. Stream Handler (Prints to screen)
console_handler = logging.StreamHandler(sys.stdout)
console_formatter = logging.Formatter('%(asctime)s - %(message)s') # Simpler format for screen
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
# ---------------------

def main():
    logger.info("Bot starting up...") # Replaces print()
    
    try:
        fetcher = DataFetcher()
        strategy = MovingAverageStrategy()
        executor = Executor()
        logger.info("Modules initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize modules: {e}")
        return

    while True:
        try:
            # 1. Fetch
            logger.info("Fetching new data...")
            df = fetcher.get_historical_data()
            
            if df is not None:
                # Log the current price for reference
                current_price = df.iloc[-1]['close']
                logger.info(f"Current Price: {current_price}")

                # 2. Analyze
                signal = strategy.analyze(df)
                
                # 3. Execute
                if signal:
                    logger.warning(f"SIGNAL DETECTED: {signal}") # Warning makes it stand out
                    executor.place_order(signal)
                    logger.info(f"Order for {signal} executed successfully.")
                else:
                    logger.info("No signal detected. Waiting...")
            
            else:
                logger.warning("Data fetch returned None.")

            time.sleep(10)

        except KeyboardInterrupt:
            logger.info("Bot stopped by user.")
            break
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()