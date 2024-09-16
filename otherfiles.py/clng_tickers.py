import pandas as pd


def main():
    
    # Column names
    columns = ["Sector"]
    path = "C:/Users/dl/Desktop/pycode/pandas_numpy/Pandas_serie/exercice3/tickers_and_names.csv"
    df_read = read_file(path)

    try:
        df_read.drop(columns=columns)
        df_read.dropna()
        df_read.to_csv("C:/Users/dl/Desktop/pycode/pandas_numpy/Pandas_serie/exercice3/done/healts.csv",
                       columns=["Ticker","Name"])
    except Exception as e:
        raise RuntimeError(f"Error indexing Date or dropping NaN: {e}")

def read_file(file_path:str)-> pd.DataFrame:
    file_read = pd.read_csv(file_path)
    df_file_read = pd.DataFrame(file_read)
    return df_file_read

main()