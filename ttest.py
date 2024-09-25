def replace_missing_value(chosen_sectors_dict: dict, old_value: str, new_value: str) -> dict:

    for sector, stocks in chosen_sectors_dict.items():
        if old_value in stocks:

            index = stocks.index(old_value)
            stocks[index] = new_value
            print(f"Replaced {old_value} with {new_value} in sector {sector}")
    
    return chosen_sectors_dict

chosen_sectors_dict = {'XLY': ['zz', 'AAGRW'], 'XLP': ['AAL', 'aa']}
updated_sectors_dict = replace_missing_value(chosen_sectors_dict, 'AAGRW', 'AAPL')
print(updated_sectors_dict)
