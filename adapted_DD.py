import yfinance as yf
from datetime import datetime, timedelta

# Function to download 5 years of data for a given ticker
failed = []
def yfin(tickers: list, sector = False):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=5*365)
    for ticker in tickers :
        print(f"Downloading data for {ticker}...")
        try:
            stock_data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
            if not stock_data.empty:
                if sector == True: 
                    stock_data.to_csv(f'C:/Users/dl/Desktop/project_portofolio_analysis/Data_base/MarketData/{ticker}.csv')
                    print(f"Data for {ticker} Sector downloaded successfully.")
                else :
                    stock_data.to_csv(f'C:/Users/dl/Desktop/project_portofolio_analysis/testing/{ticker}.csv')
                    print(f"Data for {ticker} downloaded successfully.")
            else:
                print(f"No data found for {ticker}. It might be delisted or invalid.")
                failed.append(ticker)
        except Exception as e:
            print(f"Failed to download data for {ticker}: {e}")
            failed.append(ticker)
    return failed

# Collect ticker symbols from the user

