import corr_sectors as csect
import support_functions as psf
import pandas as pd

def display_tickers(sector_dict: dict):
    # Set the path to the data folder
    folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\filtered_data\\sector"
    
    # Retrieve files (sectors) in the specified folder
    sector_files = psf.get_files_in_folder(folder_path)
    
    # Check if any files were found
    if not sector_files:
        print("No files found in the specified folder.")
        return

    # Initialize dictionaries and lists for selections
    stock_selection = {"Symbol": [], "Company_name": []}
    chosen_stocks = []
    chosen_sectors_dict = {}
    file_dict = {}

    # Index counter for tracking sector recommendations
    sector_index = 0

    # Main loop to prompt user selection mode
    while True:
        
        # Choose between predefined construction methods
        build_choice = choose_construction_method()
        
        while True:
            if build_choice == 1:
                # Use the recommended construction method
                sector_dict, sector_files = recommended_construction(sector_index, sector_dict, sector_files)
                
            elif build_choice == 2:
                # Placeholder for alternative methods (if implemented)
                pass
            
            # Display available sectors and get user choice
            user_sector_choice, file_dict = available_sectors(sector_files, sector_dict, file_dict)
            
            # Loop to construct portfolio based on user selections
            while True:
                stock_selection, chosen_sectors_dict = construct_portfolio(
                    file_dict, folder_path, chosen_stocks, chosen_sectors_dict, stock_selection, user_sector_choice
                )
                
                # Prompt user for next action
                action_choice = psf.try_again(
                    f"\n1) Add more stocks from {sector_files[user_sector_choice - 1]} Sector;\n"
                    f"2) Return to Sector Options;\n"
                    f"3) Move to Analysis;\n",index=[1, 2, 3]
                )
                
                if action_choice == 1:
                    continue
                elif action_choice == 2:
                    break
                elif action_choice == 3:
                    # Return selected stocks and sectors for analysis
                    return stock_selection, chosen_sectors_dict, build_choice
                
def value_to_filepath(sectors_dict: dict, chosen_sectors_dict: dict, tickers_dict: dict, ticker_symbol):
    """Retrieve the sector file name for a given ticker symbol."""
    if ticker_symbol in tickers_dict['Symbol']:
        index = tickers_dict['Symbol'].index(ticker_symbol)
        print(f"Found symbol: {ticker_symbol} -> {tickers_dict['Company_name'][index]}")

    for sector, tickers in chosen_sectors_dict.items():
        if ticker_symbol in tickers:
            for key, value in sectors_dict.items():
                if value == sector:
                    return key

def recommended_construction(index, sector_dict, sector_files):
    """Use recommended 5 least correlated sectors to construct the portfolio."""
    optimal_sectors = csect.optimal_sectors()
    selected_sectors = tuple(optimal_sectors.iloc[0, 0].split(', '))
    print("\nOptimum sectors combination:")

    if index == 0:
        psf.print_table(optimal_sectors)
        print("")

    filtered_sector_dict = {key: value for key, value in sector_dict.items() if value in selected_sectors}
    filtered_sector_files = [sector for sector in sector_files if sector in filtered_sector_dict.keys()]

    return filtered_sector_dict, filtered_sector_files

def choose_construction_method():
    """Prompt the user to select a portfolio construction method."""
    print("\n\n=== Choose Portfolio Construction Method:\n\n"
          "     1. Use recommended 5 least correlated sectors for diversification.\n"
          "     2. Customize by selecting sectors of your choice.")

    build_choice = psf.get_int_positive("Select Method: ", list_range=[1, 2])
    return build_choice

def construct_portfolio(file_dict: dict, folder_path, chosen_stocks: list, chosen_sectors_dict: dict, stock_selection: dict, sector_choice: int):
    """Allow user to select stocks from a chosen sector and add to portfolio."""
    while True:
        if sector_choice in file_dict.keys():
            file_path = psf.get_file_path(folder_path, file_dict[sector_choice][0], extension="csv")
            stock_data = psf.read_file(file_path).iloc[:, :2]

            if stock_data.empty:
                print("No data available in the selected file.")
                break

            try:
                result_dict = stock_data.apply(lambda row: [row.iloc[0], row.iloc[1]], axis=1).to_dict()
            except KeyError as e:
                print(f"Missing expected columns: {e}")
                break

            psf.print_table(stock_data)

            while True:
                stock_choice = psf.get_int_positive("Select stock to add: ", list_range=list(result_dict.keys()))
                selected_stock = result_dict[stock_choice]

                if selected_stock in chosen_stocks:
                    print("This stock is already in the portfolio.")
                    continue
                else:
                    chosen_stocks.append(selected_stock)
                    sector_symbol = file_dict[sector_choice][1]

                    if sector_symbol in chosen_sectors_dict:
                        chosen_sectors_dict[sector_symbol].append(selected_stock[0])
                    else:
                        chosen_sectors_dict[sector_symbol] = [selected_stock[0]]
                    break

            if stock_choice in result_dict.keys():
                stock_selection["Symbol"].append(selected_stock[0])
                stock_selection["Company_name"].append(selected_stock[1])

                print(f"\n--> Your Portfolio contains:\n\nTicker: {stock_selection['Symbol'][-1]}\n"
                      f"Company Name: {stock_selection['Company_name'][-1]}")
                return stock_selection, chosen_sectors_dict

def available_sectors(sector_files, sector_dict, file_dict):
    """Display available sectors and allow user to select one."""
    file_dict = enumerate_files(sector_files, sector_dict, file_dict)
    sector_choice = psf.get_int_positive("Choose a sector: ", list_range=list(file_dict.keys()))
    return sector_choice, file_dict

def enumerate_files(sector_files, sector_dict, file_dict):
    """Enumerate and display sector files."""
    for i, file in enumerate(sector_files, start=1):
        file_dict[i] = [file, sector_dict[file]]
        print(f"{i}) {file.strip().capitalize()}")
    return file_dict

if __name__ == "__main__":
    sectors_dict = {
        'basic_materials': 'XLB',
        'consumer_discretionary': 'XLY',
        'consumer_staples': 'XLP',
        'energy': 'XLE',
        'financials': 'XLF',
        'healthcare': 'XLV',
        'industrials': 'XLI',
        'real_estate': 'XLRE',
        'technology': 'XLK',
        'telecommunications': 'XLC',
        'utilities': 'XLU'
    }
    display_tickers(sectors_dict)
