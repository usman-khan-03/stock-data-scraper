import os
import yfinance as yf
import pandas as pd
from datetime import datetime
import time

# ======== SETTINGS ========
STOCK_FILE = "stock_symbols.txt"  # File containing your 900+ symbols
DELAY = 2  # Seconds to wait between downloads (avoid getting blocked)
START_DATE = "1900-01-01"
OUTPUT_FOLDER = "stock_data_files"

# ======== MAIN CODE ========
def get_stock_data(stock_symbol):
    """Download stock data with error handling"""
    try:
        print(f"Downloading {stock_symbol}...", end=" ", flush=True)
        data = yf.download(
            stock_symbol,
            start=START_DATE,
            end=datetime.now().strftime("%Y-%m-%d"),
            progress=False,
            auto_adjust=True
        )
        if not data.empty:
            print(f"Got {len(data)} days of data")
            return data
        else:
            print("No data available")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_to_csv(data, symbol):
    """Save data to CSV file"""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    filename = f"{OUTPUT_FOLDER}/{symbol}.csv"
    data.to_csv(filename)
    print(f"Saved to {filename}")

def load_stock_symbols():
    """Load stock symbols from file"""
    with open(STOCK_FILE) as f:
        return [line.strip() for line in f if line.strip()]

def main():
    print("\n=== YAHOO FINANCE STOCK DOWNLOADER ===")
    print(f"Data will be saved in: {os.getcwd()}/{OUTPUT_FOLDER}\n")
    
    symbols = load_stock_symbols()
    total = len(symbols)
    
    for i, symbol in enumerate(symbols, 1):
        print(f"\n[{i}/{total}] Processing {symbol}")
        data = get_stock_data(symbol)
        if data is not None:
            save_to_csv(data, symbol)
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
    print("\nAll done! Check your downloaded files.")