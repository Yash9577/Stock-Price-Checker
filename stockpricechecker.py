import requests

def get_stock_price(symbol):
    api_key = 'P5HPKI5J2GXG3ZF7' 
    base_url = "https://www.alphavantage.co/query"
    
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": api_key
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "Time Series (1min)" in data:
        latest_data = data["Time Series (1min)"]
        latest_timestamp = max(latest_data.keys())
        latest_price = latest_data[latest_timestamp]["4. close"]
        return latest_price
    else:
        return None

def main():
    company_symbol = input("Enter the company's stock symbol (e.g., AAPL): ")
    stock_price = get_stock_price(company_symbol)
    
    if stock_price is not None:
        print(f"The current stock price of {company_symbol} is ${stock_price}")
    else:
        print(f"Failed to retrieve stock price for {company_symbol}")

if __name__ == "__main__":
    main()
