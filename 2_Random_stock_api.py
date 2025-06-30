import requests
def get_stcock_data_api():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    api = response.json()
    # api = requests.get("https://api.freeapi.app/api/v1/public/stocks/stock/random").json()

    if api["success"] and "data" in api:
        stock = api["data"]
        stock_name = stock["Name"]
        stock_symbol = stock["Symbol"]
        stock_listing_date  = stock["ListingDate"]
        marketcap = stock["MarketCap"]
        stock_price = stock["CurrentPrice"]
        stock_high_low = stock["HighLow"]
        stock_dividendYield = stock["DividendYield"]
        stock_roce = stock["ROCE"]
        stock_roe = stock["ROE"]
        return stock_name, stock_symbol, stock_listing_date, marketcap, stock_price, stock_high_low, stock_dividendYield, stock_roce, stock_roe
    else:
        raise Exception("Failed to retrieve stock data from API")

def main():
    try:
        stock_name, stock_symbol, stock_listing_date, marketcap, stock_price, stock_high_low, stock_dividendYield, stock_roce, stock_roe = get_stcock_data_api()
        print(f"Stock Name: {stock_name}")
        print(f"Stock Symbol: {stock_symbol}")
        print(f"Stock Listing Date: {stock_listing_date}")
        print(f"Stock Market Cap: {marketcap}")
        print(f"Stock Price: {stock_price}")
        print(f"Stock High Low: {stock_high_low}")
        print(f"Stock Dividend Yield: {stock_dividendYield}")
        print(f"Stock ROCE: {stock_roce}")
        print(f"Stock ROE: {stock_roe}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

