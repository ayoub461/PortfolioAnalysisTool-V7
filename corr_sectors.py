import numpy as np
from adapted_DD import yfin
import Support_funct as psf
import pandas as pd



def optimal_sectors ():

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

    ticker_sector = ['XLB', 'XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLRE', 'XLK', 'XLC', 'XLU']


    folder_path  = "C:/Users/dl/Desktop/project_portofolio_analysis/filterd_data/sector/sector_data"

    # Initialize a dictionary to store daily returns
    daily_returns_dict = {}

    # Loop through each sector and file
    for ticker in sectors_dict.values():
        
        #file name format
        file_name = f"{ticker}.csv"
        #read file
        file_path = psf.get_file_path(folder_path,ticker)
        df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
        # Calculate daily returns
        df['Daily Return'] = df['Adj Close'].pct_change().shift(-1) * 100
        # Store daily returns in the dictionary
        daily_returns_dict[ticker] = df['Daily Return']

    # Create a DataFrame from the daily returns dictionary
    returns_df = pd.DataFrame(daily_returns_dict)
    # Calculate correlation matrix
    correlation_matrix = returns_df.corr()

    #all possible combinations
    all_combinations = psf.combinations(ticker_sector, 5)


    #store the least correlated combination
    combo_dict = {"":[]}
    min_combo = 1
    min_combo_dict = {}

    for combo in all_combinations :
        #sumup the pair corr.
        sumup = 0    
        #pair corr
        pairs = psf.combinations(combo, 2)
        
        for pair in pairs:
            
            #unpack the pair
            sector1, sector2 = pair
            #calulate abs value for each pair corr
            if sector1 in correlation_matrix.columns and sector2 in correlation_matrix.index:
                value = correlation_matrix.loc[sector1, sector2]
                abs_value = abs(value) 
                sumup += abs_value
            else:
                print(f"Pair {sector1}, {sector2} not found in correlation matrix")
        
        if len(pairs) > 0:        
            #calculate and store average correlation
            average_correlation = sumup / len(pairs)
            combo_dict[combo] = average_correlation
            #check the min average correlation
            if average_correlation < min_combo :
                min_combo = average_correlation
                sectors_string = ', '.join(combo)
                min_combo_dict = {sectors_string:average_correlation}
            else :
                continue

        else:
            print(f"No valid pairs found for combo: {combo}")

    #Into Data frames
    df_combo = pd.DataFrame(list(combo_dict.items()), columns=['combination', 'average'])
    df_min_combo = pd.DataFrame(list(min_combo_dict.items()), index=['Correlation'], columns=['Combination', 'min average absolute '])

    #into excel files
    save_to_file = 'sector correlations'
    pathf = psf.get_file_path("C:/Users/dl/Desktop/project_portofolio_analysis",save_to_file,"xlsx")
    with pd.ExcelWriter(pathf) as writer:
        correlation_matrix.to_excel(writer, sheet_name="Pairs Correlation Matrix")
        df_combo.to_excel(writer, sheet_name='Sector Combinations')
        df_min_combo.to_excel(writer,sheet_name='Optimal Combination')

    return df_min_combo
    
    