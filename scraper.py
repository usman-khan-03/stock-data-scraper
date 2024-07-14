import io
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import json
import re

def get_stock_data(stock_symbol):
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{stock_symbol}?period1=0&period2={int(datetime.datetime.now().timestamp())}&interval=1d&events=history&includeAdjustedClose=true'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        df = pd.read_csv(io.StringIO(response.text))
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    else:
        raise ValueError(f"Failed to retrieve data. Status code: {response.status_code}")
    
    # soup = BeautifulSoup(response.text, 'html.parser')
    
    # # Find the script tag with the required data
    # script_tag = soup.find('script', string=re.compile('root.App.main'))
    
    # if not script_tag:
    #     raise ValueError("Couldn't find the script tag containing the data.")
    
    # # Extract JSON data from the script tag
    # json_text = script_tag.string
    # json_data = json.loads(re.search(r'root.App.main\s*=\s*({.*?});', json_text).group(1))
    
    # # Extract the historical data
    # prices = json_data['context']['dispatcher']['stores']['HistoricalPriceStore']['prices']
    
    # # Create DataFrame from the extracted data
    # df = pd.DataFrame(prices)
    
    # # Drop rows without valid 'type' field
    # df = df[df['type'].isna()]
    
    # # Select relevant columns and rename them
    # df = df[['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']]
    # df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    
    # # Convert timestamp to datetime
    # df['Date'] = pd.to_datetime(df['Date'], unit='s')
    
    # return df

def save_to_csv(df, stock_symbol):
    file_name = f'{stock_symbol}_historical_data.csv'
    df.to_csv(file_name, index=False)
    print(f'Data saved to {file_name}')

if __name__ == "__main__":
    stock_symbol = 'RIG'  # Replace with the stock symbol you want to scrape
    try:
        df = get_stock_data(stock_symbol)
        save_to_csv(df, stock_symbol)
    except ValueError as e:
        print(e)

