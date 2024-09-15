import exercice3.version4.adapted_DD as dd
import Support_funct as psf
import pandas as pd

"""Check and Display existing Tickers"""

folder_path = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\major index"
    
f_files = psf.get_files_in_folder(folder_path)
file= f_files[0]
print(file)

if not f_files:
    print("No files found in the specified folder.")
    

file_path = psf.get_file_path(folder_path,file)
file_read = pd.read_csv(file_path)

print(file)

tickers = file_read.iloc[0:len(file_read), 0]

failed = dd.yfin(tickers)

failed_df = pd.DataFrame(failed, columns=["tickers"])

file_folder = "C:\\Users\\dl\\Desktop\\project_portofolio_analysis\\testing"

fpath = psf.get_file_path(file_folder,"failed_tickers", extension="xlsx")

with pd.ExcelWriter(fpath, mode='a') as writer:
    failed_df.to_excel(writer, sheet_name='Third_list')
