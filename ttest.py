import corr_sectors as csect
import Support_funct as psf
import pandas as pd
from typing import Any, List, Dict, Tuple

def displayTik(sector_dict: Dict[str, str]) -> Dict:
    """Check and Display existing Tickers"""

    folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\filterd_data\\sector"
    
    f_files = psf.get_files_in_folder(folder_path)
    if not f_files:
        print("No files found in the specified folder.")
        return {}
    
    file_dict = {}
    choice_dict = {"Symbol": [], "Company_name": []}
    chosen_stocks = []
    chosen_sectors_dict = {}
    i = 0

    while True:
        print("\n\n===Choose how to build your portfolio:\n\n"
              "     1. Use our recommended 5 least correlated sectors for diversification.\n"
              "     2. Customize by selecting your preferred number and choice of sectors.")

        build_choice = psf.get_int_positive("\nWhich Method you choose: ", list_range=[1, 2])
        while True :
            if build_choice == 1:
                optimum_sect = csect.optimal_sectors()
                sectors_tuple = tuple(optimum_sect.iloc[0, 0].split(', '))
                print("\nOptimum sectors combination is:")

                if i == 0:
                    psf.print_table(optimum_sect)
                    print("")
                    i += 1
            
                filtered_sectors_dict = {key: value for key, value in sector_dict.items() if value in sectors_tuple}
                f_files = [sector for sector in f_files if sector in filtered_sectors_dict.keys()]
                
                sector_dict = filtered_sectors_dict
            
            elif build_choice == 2:
                pass  # Implement custom selection logic here if needed

            file_dict = enumerate_files(f_files, sector_dict, file_dict)
            user_sector_choice = psf.get_int_positive("\nChoose a Sector: ", list_range=list(file_dict.keys()))

            while True:
                choices_dict, chosen_sectors_dict = construct_port(file_dict, folder_path, chosen_stocks, chosen_sectors_dict, choice_dict, user_sector_choice)
                
                choice = psf.try_again(
                    f"\n1) Add more stocks from {f_files[user_sector_choice-1]} Sector;\n"
                    f"2) Return to Sector Options;\n"
                    f"3) Move to Analysis;\n",
                    index=[1, 2, 3]
                )

                if choice == 1:
                    continue
                elif choice == 2:
                    break
                elif choice == 3:
                    return choices_dict, chosen_sectors_dict

def construct_port(file_dict: Dict[int, List[str]], folder_path: str, chosen_stocks: List, chosen_sectors_dict: Dict[Any, List], choice_dict: Dict[str, List], user_sector_choice: int) -> Tuple[Dict, Dict]:
    # Display available stocks in sector
    while True:
        if user_sector_choice in file_dict.keys():
            file_path = psf.get_file_path(folder_path, file_dict[user_sector_choice][0], extension="csv")
            file_read0 = psf.read_file(file_path)
            file_read = file_read0.iloc[:, :2]

            if file_read.empty:
                print("No data available in the selected file.")
                break

            try:
                result_dict = file_read.apply(lambda row: [row.iloc[0], row.iloc[1]], axis=1).to_dict()
            except KeyError as e:
                print(f"Missing expected columns: {e}")
                break

            psf.print_table(file_read)

            while True:
                user_stock_choice = psf.get_int_positive("\n\n|->Which stock to add: ", list_range=list(result_dict.keys()))

                if result_dict[user_stock_choice] in chosen_stocks:
                    print("This Stock is Already chosen;")
                    continue
                else:
                    chosen_stocks.append(result_dict[user_stock_choice])

                    sector_symbol = file_dict[user_sector_choice][1]

                    # Append the stock symbol to the existing list or start a new list
                    if sector_symbol in chosen_sectors_dict:
                        chosen_sectors_dict[sector_symbol].append(result_dict[user_stock_choice][0])
                    else:
                        chosen_sectors_dict[sector_symbol] = [result_dict[user_stock_choice][0]]
                    break

            if user_stock_choice in result_dict.keys():
                choice_dict["Symbol"].append(result_dict[user_stock_choice][0])
                choice_dict["Company_name"].append(result_dict[user_stock_choice][1])

                print(f"""\n-->Your Choice Symbol: {choice_dict["Symbol"]} : {choice_dict["Company_name"]} """)

                return choice_dict, chosen_sectors_dict

def enumerate_files(f_files: List[str], sector_dict: Dict, file_dict: Dict) -> Dict:
    # Print sectors
    for i, file in enumerate(f_files, start=1):
        file_dict[i] = [file, sector_dict.get(file, '')]
        file = file.strip().capitalize()
        print(f"{i}) {file}")

    return file_dict

if __name__ == "__main__":
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
    displayTik(sectors_dict)
