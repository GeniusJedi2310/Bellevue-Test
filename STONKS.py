def main():
    stocks = {
        'AAPL': 150.25,
        'GOOGL': 2500.50,
        'MSFT': 300.75,
        'AMZN': 3500.00,
        'TSLA': 700.25,
        'FB': 350.50,
        'NFLX': 600.75,
        'NVDA': 750.00,
        'PYPL': 250.25,
        'INTC': 55.75,
        'AMD': 120.00,
        'CRM': 300.50,
        'DIS': 180.75,
        'UBER': 45.50,
        'V': 250.00
    }

 
    ticker = input("Enter a stock ticker symbol: ")

 
    if ticker in stocks:
        price = stocks[ticker]
        print(f"Ticker Symbol: {ticker}")
        print(f"Stock Price: ${price}")
    else:
        print("Ticker symbol not found.")

if __name__ == '__main__':
    main()
