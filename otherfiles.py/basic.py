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
    
chosen_sectors_dict = {'XLY': ['AAL', 'AAN'], 'XLP': ['AAGRW']}
tickers_dict = {'Symbol': ['AAL', 'AAGRW'], 'Company_name': ['American Airlines Group Inc. Common Stock', 'African Agriculture Holdings Inc. Warrant']}

file_input = 'AAGRW'
index = 0

if file_input in tickers_dict['Symbol']:
    index = tickers_dict['Symbol'].index(file_input)
    print(f"Found symbol: {file_input} -> {tickers_dict['Company_name'][index]}")

    # Find the sector associated with this ticker in chosen_sectors_dict
    for key1, value1 in chosen_sectors_dict.items():
        if file_input in value1:
            # Find the sector name in sectors_dict
            for key2, value2 in sectors_dict.items():
                if value2 == key1:
                    print(f"The sector for {file_input} is: {key2}")
                    break
            
            
            