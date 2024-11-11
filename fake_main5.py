from pandas import DataFrame, errors
import financial_functions as ff
import version5.support_functions as psf
import download_data as DD
import version5.display_tickers as DST
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
    
    #DST.displayTik() returns a list of tickers
    tickers_dict, chosen_sectors_dict, build_choice = DST.displayTik(sectors_dict)
    
    # Get the number of elements in the list
    num_elements = len(tickers_dict["Symbol"])
    

    #Create a Data frame for tickers in the portofolio
    df_tickers_dict = DataFrame(tickers_dict)
    df_tickers_dict.index += 1


    #Print portofolio Containt
    print("\n====>Your portofolio contains : \n")
    psf.print_table(df_tickers_dict)
    

    #Variables
    weights = []
    files = []   
    closing = {}
    path_Data_base = 'C:/Users/dl/Desktop/project_portofolio_analysis/Data_base'
    path_saving_folder = 'C:/Users/dl/Desktop/project_portofolio_analysis'


    print("\n\n====> Processing files...\n")
    for i in range(num_elements ):
        #ClCollecting Data
        files,file_input,df_file_read, weights = collect_Data(i, tickers_dict, path_Data_base, files, weights, num_elements, sectors_dict, chosen_sectors_dict )

        # Cleaning Data
        closing_df0 = clean_Data(closing, file_input, i, df_file_read)

    #Analyzing Data
    closing_df1, df_correlation, df_portfolio, df_sector_DL0 = analyse_Data(closing_df0, weights, chosen_sectors_dict)
    

    #saving Data
    psf.save_data(closing_df1, df_correlation, df_portfolio, path_saving_folder, df_sector_DL0)


def collect_Data(index : int, tickers_dict:dict, path_Data_base: str,
                    files : list, weights: list, num_elements: int,
                    sectors_dict : dict, chosen_sectors_dict: dict) -> Tuple[list,str,DataFrame, list]:

    while True:
        
        try:
            #Assinging tickers as input
            file_input = tickers_dict["Symbol"][index]

            #Check if file exists or needs to be downloaded
            if psf.check_exsiting_file(file_input, path_Data_base) == True :
                file_path = psf.get_file_path(path_Data_base, file_input, extension="csv")
                
            else :
                status = DD.yfin(file_input)
                
                if status == True :
                    
                    file_path = psf.get_file_path(path_Data_base, file_input, extension="csv")
                
                elif status == False :
                    
                    #get file sector name
                    sectors_folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\filterd_data\\sector"
                    sector_name = DST.Value_to_FilePath(sectors_dict, chosen_sectors_dict, tickers_dict, file_input)

                    #Remove the invalid ticker
                    tickers_dict['Symbol'].pop(index)
                    tickers_dict['Company_name'].pop(index)
                    print(f"ticker dict2 : {tickers_dict}")                 
                    print(f"index : {index}")
                    
                    #Read the file                                        
                    sectors_file_path = psf.get_file_path(sectors_folder_path, sector_name)
                    sector_read = psf.read_file(sectors_file_path)
                    psf.print_table(sector_read.iloc[:,:2])
                    
                    print(f"Failed to download data for {file_input}")
                    print("Please choose another stock.")
                    
                    user_stock_choice = psf.get_int_positive("\n\n|->which stock to add : ", list_range=list(range(1,len(sector_read)+1)))
                    
                    chosen_value_col1 = sector_read.iloc[user_stock_choice-1, 0]  
                    chosen_value_col2 = sector_read.iloc[user_stock_choice-1, 1]  
                    
                    tickers_dict["Symbol"].append(chosen_value_col1)
                    tickers_dict["Company_name"].append(chosen_value_col2)  
                    
                    chosen_sectors_dict = psf.replace_missing_ticker(chosen_sectors_dict, file_input, chosen_value_col1)
                    return collect_Data(index, tickers_dict, path_Data_base, files, weights, num_elements, sectors_dict, chosen_sectors_dict)
                    

            #Append files[] with the file input
            files.append(file_input)

            #read file input
            df_file_read = psf.read_file(file_path)
            print(df_file_read.shape)

            weight = psf.get_valid_weight(file_input, weights, num_elements, index)
            weights.append(weight)
            
            return (files,file_input,df_file_read, weights)
        
        #Cheking reading Errors
        except (FileNotFoundError, PermissionError):
            print(f"Error reading file: {file_path}. Please ensure the file exists and is accessible.")
            continue

        #Cheking Empty Errors
        except errors.EmptyDataError:
            print(f"Empty data: {file_path}. The file is empty.")
            continue

        #Cheking Parsing Errors
        except errors.ParserError:
            print(f"Parsing error: {file_path}. The file content is not properly formatted.")
            continue
        
def clean_Data(closing: dict,
               file_input:str,
                   index: int,
                     df_file_read: DataFrame)-> DataFrame:

    
    #set 'Date'coloum in the first data frame as Index, if it fails, try it with next Data.F
    if not psf.set_date(closing, df_file_read, index):
        return
    else :
        closing = psf.set_date(closing, df_file_read, index)

    #formating 'Adj Close' as numeric value
    closing_df = psf.set_closing_prices(closing, df_file_read, file_input)

    return closing_df

def analyse_Data(closing_df0 : DataFrame,
                  weights: list, chosen_sectors_dict : dict)->Tuple[DataFrame, DataFrame, DataFrame, DataFrame]:

    #Dropping NaN
    closing_df01 = psf.prepare_closing_df(closing_df0)
    
    #calculate daily return
    df_dict, closing_df02  = ff.calculate_daily_returns(closing_df01) 

    #calculate daily return of market
    portfolio_sector, df_sector_DL, df_sector_DL0 = ff.market_DR(chosen_sectors_dict)

    #calculate beta :    
    beta_results = ff.calculate_beta(df_sector_DL, closing_df02, chosen_sectors_dict)
    
    medaf_return  = ff.medaf(portfolio_sector, beta_results, chosen_sectors_dict)
    
    #Calculate the risk of each stock
    risk_dict =  ff.risk_stock (closing_df02)

    #calculate Cumulative return for each stock
    closing_df1, totals_Cu_Rre = ff.calculate_cumulative_returns(closing_df02)
    
    #calculate the Annulized return
    number_ofDays = psf.days_number(closing_df1)
    five_year_annualized = ff.annulized_return(totals_Cu_Rre,number_ofDays)

    #calculate Correlation between Stocks
    df_correlation = ff.calculate_correlation(closing_df1)

    #calculate Portofolio return
    df_portfolio = ff.recap_portfolio(df_dict, weights, risk_dict, five_year_annualized, beta_results, medaf_return)

    return (closing_df1, df_correlation, df_portfolio, df_sector_DL0)

if __name__ == "__main__":
    main()
