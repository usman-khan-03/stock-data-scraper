# Stock Data Scraper

A Python script to scrape historical stock data from Yahoo Finance and save it as a CSV file.

## Prerequisites
- Python 3.x
- Git

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/usman-khan-03/stock-data-scraper.git
    cd stock-data-scraper
    ```

2. **Create and Activate a Virtual Environment**:
    - On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install Required Libraries**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Modify the Script**:
    - Open `scraper.py` and replace `'BRK-B'` with the desired stock symbol.

2. **Run the Script**:
    ```sh
    python scraper.py
    ```

3. **Output**:
    - The historical data will be saved in a CSV file named `{stock_symbol}_historical_data.csv` in the project directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)