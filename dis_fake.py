import corr_sectors as csect
import Support_funct as psf
import pandas as pd

def displayTik(sector_dict :dict)->dict:

    """Check and Display existing Tickers"""

    folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\filterd_data\\sector"
    
    f_files = psf.get_files_in_folder(folder_path)
    if not f_files:
        print("No files found in the specified folder.")
        return
    
    file_dict = {}
    choice_dict = {"Symbol":[],
                   "Company_name":[]}
    '''
    Available_Sectors = {
        'Aerospace': 'ITA',  #(Space/Defense)
        'Banking': 'XLF',  # JPMorgan Chase & Co. (Banking)
        'Healths': 'XLV',  # Pfizer Inc. (Health)
        'Techology': 'XLK'  # Apple Inc. (Technology)
    }
    '''
    chosen_stocks = []
    chosen_sectors_dict = {}
    

    
    
    while True:
    
        print("\n\n===Choose how to build your portfolio:\n\n"
            "     1. Use our recommended 5 least correlated sectors for diversification.\n"
            "     2. Customize by selecting your preferred number and choice of sectors.")
    
        build_choice = psf.get_int_positive("\nWhich Methode you choose: ",list_range=[1,2])
        
        while True : 
            if build_choice == 1 :
                optimum_sect = csect.optimal_sectors()
                sectors_tuple = tuple(optimum_sect.iloc[0,0].split(', '))
                
                print("\noptimum sectors combination is :")
                psf.print_table(optimum_sect)
                break

            elif build_choice == 2 :
                ...
            else :
                continue
    
        #printing secotrs
        for i, file in enumerate(f_files, start=1):
            file_dict[i] = [file, sector_dict[f"{file}"]]
            file = file.strip().capitalize()
            print(f"{i}) {file}")
            
                    
        # Prompt user for a sector
        user_sector_choice = psf.get_int_positive("\nChoose a Sector : ", list_range=list(file_dict.keys()))

        # Display available stocks in sector
        while True :
            if user_sector_choice in file_dict.keys():
                
                file_path = psf.get_file_path(folder_path, file_dict[user_sector_choice][0], extension="csv")
                file_read0 = psf.read_file(file_path)
                file_read = file_read0.iloc[:,:2]
                
                                
                if file_read.empty:
                    print("No data available in the selected file.")
                    break
                
                try:
                    result_dict = file_read.apply(lambda row: [row.iloc[0], row.iloc[1]], axis=1).to_dict()
                except KeyError as e:
                    print(f"Missing expected columns: {e}")
                    break
                
                psf.print_table(file_read)
            #get_user choice (indexing)
                while True :
                    user_stock_choice = psf.get_int_positive("\n\n|->which stock to add : ", list_range=list(result_dict.keys()))
                    
                    if result_dict[user_stock_choice] in chosen_stocks :
                            print("This Stock is Already chosen;")
                            continue
                    else:
                        chosen_stocks.append(result_dict[user_stock_choice])
                        
                        sector_symbol = file_dict[user_sector_choice][1]
                    
                        # If the sector already exists in the dictionary, append to the list, otherwise create a new list
                        if sector_symbol in chosen_sectors_dict:
                            chosen_sectors_dict[sector_symbol].append(result_dict[user_stock_choice][0])
                        else:
                            chosen_sectors_dict[sector_symbol] = [result_dict[user_stock_choice][0]]
                        break
                        
                if user_stock_choice in result_dict.keys():
  
                    choice_dict["Symbol"].append(result_dict[user_stock_choice][0])
                    choice_dict["Company_name"].append(result_dict[user_stock_choice][1])
                    
                    print(f"""\n-->Your Choice Symbole  : {choice_dict["Symbol"][-1]} : {choice_dict["Company_name"][-1]} """)

                    choice = psf.try_again(f"\n1) Add more stocks from {f_files[user_sector_choice-1]} Sector;\n"
                                    f"2) Return to Sector Options;\n"
                                    f"3) Move to Analysis;\n",index=[1,2,3])
                    if choice == 1:
                        continue
                    elif choice == 2 :
                        break
                    elif choice == 3 :
                        return (choice_dict, chosen_sectors_dict)           


    
if __name__ == "__main__":
    displayTik()
