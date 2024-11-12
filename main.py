from pandas import DataFrame, errors
import financial_functions as ff
import support_functions as psf
import download_data as dd
import display_tickers as dst
from typing import Tuple

def main():
    sectors_dict = {
        'basic_materials': 'XLB',  # Materials Select Sector SPDR Fund
        'consumer_discretionary': 'XLY',  # Consumer Discretionary Select Sector SPDR Fund
        'consumer_staples': 'XLP',  # Consumer Staples Select Sector SPDR Fund
        'energy': 'XLE',  # Energy Select Sector SPDR Fund
        'financials': 'XLF',  # Financial Select Sector SPDR Fund
        'healthcare': 'XLV',  # Health Care Select Sector SPDR Fund
        'industrials': 'XLI',  # Industrial Select Sector SPDR Fund
        'real_estate': 'XLRE',  # Real Estate Select Sector SPDR Fund
        'technology': 'XLK',  # Technology Select Sector SPDR Fund
        'telecommunications': 'XLC',  # Communication Services Select Sector SPDR Fund
        'utilities': 'XLU'  # Utilities Select Sector SPDR Fund
    }
    
    # dst.display_tickers() returns a dictionary of selected tickers
    tickers_dict, chosen_sectors_dict, build_choice = dst.display_tickers(sectors_dict)
    print(chosen_sectors_dict)
    print(tickers_dict)
    
    # Get the number of elements in the list
    num_elements = len(tickers_dict["Symbol"])

    # Create a DataFrame for tickers in the portfolio
    df_tickers_dict = DataFrame(tickers_dict)
    df_tickers_dict.index += 1

    # Print portfolio content
    print("\n====> Your portfolio contains: \n")
    psf.print_table(df_tickers_dict)
    
    # Variables
    weights = []
    files = []   
    closing = {}
    data_base_path = 'C:/Users/dl/Desktop/project_portofolio_analysis/Data_base'

    saving_folder_path = 'C:/Users/dl/Desktop/project_portofolio_analysis'

    print("\n\n====> Processing files...\n")
    for i in range(num_elements):
        # Collecting Data
        files, file_input, df_file_read, weights = collect_data(i, tickers_dict, data_base_path, files, weights, num_elements, sectors_dict, chosen_sectors_dict)
        
        print(f"Files: {files}")
        print(f"File Input: {file_input}")
        print(f"File Read: {df_file_read}")
        print(f"Weights: {weights}")
        print(f"Chosen Sectors Dict: {chosen_sectors_dict}")
        print(f"Tickers Dict: {tickers_dict}")
        
        # Cleaning Data
        closing_df0 = clean_data(closing, file_input, i, df_file_read)

    # Analyzing Data
    closing_df1, df_correlation, df_portfolio, df_sector_data = analyze_data(closing_df0, weights, chosen_sectors_dict)
    
    # Saving Data
    psf.save_data(closing_df1, df_correlation, df_portfolio, saving_folder_path, df_sector_data)


def collect_data(index: int, tickers_dict: dict, data_base_path: str,
                 files: list, weights: list, num_elements: int,
                 sectors_dict: dict, chosen_sectors_dict: dict) -> Tuple[list, str, DataFrame, list]:

    while True:
        try:
            print(f"Ticker dictionary (initial): {tickers_dict}")
            print(f"Index: {index}")
            
            # Assign ticker as input
            file_input = tickers_dict["Symbol"][index]
            print(f"Ticker dictionary (after assigning file_input): {tickers_dict}")
            print(f"Index: {index}")

            # Check if file exists or needs to be downloaded
            if psf.check_existing_file(file_input, data_base_path):
                file_path = psf.get_file_path(data_base_path, file_input, extension="csv")
            else:
                status = dd.yfin(file_input)
                
                if status:
                    file_path = psf.get_file_path(data_base_path, file_input, extension="csv")
                else:
                    print(f"Failed to download data for {file_input}. Please choose another stock.")
                    
                    # Get sector folder path
                    sectors_folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\filtered_data\\sector" 
                    sector_name = dst.value_to_filepath(sectors_dict, chosen_sectors_dict, tickers_dict, file_input)

                    # Remove the invalid ticker
                    tickers_dict['Symbol'].pop(index)
                    tickers_dict['Company_name'].pop(index)
                    print(f"Ticker dictionary (after removing invalid ticker): {tickers_dict}")                 
                    print(f"Index: {index}")
                    
                    # Read the file                                      
                    sectors_file_path = psf.get_file_path(sectors_folder_path, sector_name)
                    sector_data = psf.read_file(sectors_file_path)
                    psf.print_table(sector_data.iloc[:, :2])
                    
                    user_stock_choice = psf.get_int_positive("\n\n|-> Which stock to add: ", list_range=list(range(1, len(sector_data) + 1)))
                    
                    chosen_value_symbol = sector_data.iloc[user_stock_choice - 1, 0]  
                    chosen_value_company = sector_data.iloc[user_stock_choice - 1, 1]  
                    
                    tickers_dict["Symbol"].append(chosen_value_symbol)
                    tickers_dict["Company_name"].append(chosen_value_company)  
                    print(f"Ticker dictionary (after appending chosen stock): {tickers_dict}")
                    chosen_sectors_dict = psf.replace_missing_ticker(chosen_sectors_dict, file_input, chosen_value_symbol)
                    
                    # Retry with updated data
                    return collect_data(index, tickers_dict, data_base_path, files, weights, num_elements, sectors_dict, chosen_sectors_dict)
            
            # Append file to files list
            files.append(file_input)

            # Read the file
            df_file_read = psf.read_file(file_path)

            # Get valid weight
            weight = psf.get_valid_weight(file_input, weights, num_elements, index)
            weights.append(weight)

            print(files)
            print(file_input)
            
            return files, file_input, df_file_read, weights
        
        # Checking for reading errors
        except (FileNotFoundError, PermissionError):
            print(f"Error reading file: {file_path}. Please ensure the file exists and is accessible.")
            continue

        # Checking for empty file errors
        except errors.EmptyDataError:
            print(f"Empty data: {file_path}. The file is empty.")
            continue

        # Checking for parsing errors
        except errors.ParserError:
            print(f"Parsing error: {file_path}. The file content is not properly formatted.")
            continue

        
def clean_data(closing: dict, file_input: str, index: int, df_file_read: DataFrame) -> DataFrame:
    
    # Set 'Date' column in the first DataFrame as index; if it fails, try with the next DataFrame.
    if not psf.set_date(closing, df_file_read, index):
        return
    else:
        closing = psf.set_date(closing, df_file_read, index)

    # Format 'Adj Close' as a numeric value
    closing_df = psf.set_closing_prices(closing, df_file_read, file_input)

    return closing_df


def analyze_data(closing_df0: DataFrame, weights: list, chosen_sectors_dict: dict) -> Tuple[DataFrame, DataFrame, DataFrame, DataFrame]:

    # Drop NaN values
    closing_df_cleaned = psf.prepare_closing_df(closing_df0)
    
    # Calculate daily returns
    daily_return_dict, closing_df_returns = ff.calculate_daily_returns(closing_df_cleaned) 

    # Calculate daily return of market for each sector
    portfolio_sector, df_sector_daily_return, df_sector_initial = ff.market_DR(chosen_sectors_dict)

    # Calculate beta values
    beta_results = ff.calculate_beta(df_sector_daily_return, closing_df_returns, chosen_sectors_dict)
    
    # Calculate expected returns based on CAPM (Medaf)
    capm_return = ff.medaf(portfolio_sector, beta_results, chosen_sectors_dict)
    
    # Calculate the risk (volatility) of each stock
    risk_dict = ff.risk_stock(closing_df_returns)

    # Calculate cumulative return for each stock
    closing_df_cumulative, cumulative_totals = ff.calculate_cumulative_returns(closing_df_returns)
    
    # Calculate the annualized return over a five-year period
    num_days = psf.days_number(closing_df_cumulative)
    five_year_annualized = ff.annulized_return(cumulative_totals, num_days)

    # Calculate the correlation between stocks
    df_correlation = ff.calculate_correlation(closing_df_cumulative)
    
    # Print intermediate results for verification
    print(f"Cumulative Totals: {cumulative_totals}")    
    print(f"Daily Returns: {daily_return_dict}")
    print(f"Weights: {weights}")
    print(f"Risk (Volatility): {risk_dict}")
    print(f"Five-Year Annualized Return: {five_year_annualized}")
    print(f"Beta Results: {beta_results}")
    print(f"CAPM Return: {capm_return}")
    
    # Calculate portfolio return summary
    df_portfolio = ff.recap_portfolio(daily_return_dict, weights, risk_dict, five_year_annualized, beta_results, capm_return)

    return (closing_df_cumulative, df_correlation, df_portfolio, df_sector_initial)

if __name__ == "__main__":
    main()
