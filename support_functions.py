import os
from fractions import Fraction
from pandas import DataFrame, read_csv, to_datetime, to_numeric, ExcelWriter
from tabulate import tabulate
from typing import Union
import itertools


def combinations(values: list, number_elements: int):
    values_list = values  # Replace with your actual set of 11 values
    p_combinations = list(itertools.combinations(values_list, number_elements))
    return p_combinations


def days_number(df_cleaned: DataFrame) -> int:
    total_days = (df_cleaned.index[-1] - df_cleaned.index[0]).days
    return total_days


def Q_clean(file: str, folder_path: str) -> DataFrame:
    try:
        file_path = get_file_path(folder_path, file, extension="csv")
        file_read = read_file(file_path)
        file_read.drop(columns=file_read.columns[0], axis=1, inplace=True)
    except Exception as e:
        print(f"Error in Q_clean: {e}")
        raise
    return file_read


def quick_clean(to_data_fram, dropna: bool = True, fillna_value=None, 
                convert_dtypes: bool = True) -> DataFrame:
    try:
        # Attempt to convert the input to a DataFrame
        df_to_data_fram = DataFrame(to_data_fram)
        
        # Handle missing values
        if fillna_value is not None:
            df_to_data_fram.fillna(fillna_value, inplace=True)
        elif dropna:
            df_to_data_fram.dropna(inplace=True)
        
        # Convert columns to the best possible dtypes
        if convert_dtypes:
            df_to_data_fram = df_to_data_fram.convert_dtypes()

        return df_to_data_fram
    except ValueError as e:
        raise ValueError(f"Input data cannot be converted to a DataFrame: {e}")
    except TypeError as e:
        raise TypeError(f"Unsupported input data type for DataFrame conversion: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred during DataFrame conversion: {e}")



def replace_missing_ticker(chosen_sectors_dict: dict, old_value: str, new_value: str) -> dict:
    for sector, stocks in chosen_sectors_dict.items():
        if old_value in stocks:
            index = stocks.index(old_value)
            stocks[index] = new_value
    return chosen_sectors_dict


def print_table(file_read: Union[DataFrame, list]) -> str:
    print(tabulate(file_read, headers='keys', tablefmt='psql'))


def get_files_in_folder(folder_path: str) -> list:
    files_list = []
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and ".csv" in filename:
                filename = filename.replace(".csv", "")
                files_list.append(filename)
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except PermissionError:
        print(f"Permission denied: {folder_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return files_list

def get_int_positive(prompt: str = "Positive Integer:", list_range: list[int] = None) -> int:
    while True:
        try:
            x = int(input(prompt))
            if x <= 0:
                print("Please enter a positive value.")
                continue
            if list_range is not None and x not in list_range:
                print(f"Choose a value between {list_range[0]} and {list_range[-1]}")
                continue
        except KeyboardInterrupt:
            print("Program is interrupted.")
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue
        except Exception as e:
            print(f"General exception detected: {e}")
            break
        else:
            return x

def get_int(prompt: str = "Integer:") -> int:
    if not isinstance(prompt, str):
        raise KeyError("A parameter is not a string: code 3")
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        except KeyboardInterrupt:
            print("Program is interrupted.")
            break
        except Exception as e:
            print(f"General exception detected: {e}")
            break
        else:
            return x

def get_float_positive(prompt: str = "A positive Float (Decimal Or Fractional): ") -> float:
    if not isinstance(prompt, str):
        raise KeyError("A parameter is not a string: code 3")
    while True:
        try:
            x_input = input(prompt).strip()
            if '/' in x_input:
                x = float(Fraction(x_input))
            else:
                try:
                    x = float(x_input)
                except ValueError:
                    print("FloatingPointError: Not a float number.")
                    continue
            if x <= 0:
                print("Please enter a valid positive value.")
                continue
        except Exception as e:
            print(f"Please enter a valid numeric value: {e}")
            continue
        else:
            return x

def get_percentage(prompt: str = "Rate:") -> float:
    if not isinstance(prompt, str):
        raise KeyError("A parameter is not a string: code 3")
    while True:
        try:
            x = get_float_positive(prompt)
            if x > 1:
                print(f"Your choice is greater than 100%: {x}.")
                ta = try_again("Confirm this choice:\n1) Yes\n2) No")
                if ta == 1:
                    return x
                elif ta == 2:
                    continue
            return x
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Program is interrupted")
        except Exception as e:
            raise e(f"Error {e}")

def try_again(prompt: str = "Do you want to try again?", index: list[int] = [1, 2]) -> int | None:
    if not all(isinstance(i, int) for i in index):
        raise KeyError("A parameter is not a list of integers: code 2")
    list_length = len(index)
    if list_length == 0:
        raise IndexError("List is empty: code 3")
    elif list_length == 1:
        return index[0]
    while True:
        choice = get_int_positive(f"{prompt}\n\nChoice: ")
        for i in index:
            try:
                if choice == i:
                    return i
                elif i == index[list_length - 1]:
                    print(f"'{choice}' does not exist.")
                    break
            except Exception as e:
                raise e(f"Support function error: code 1: {e}: code 4")

def check_existing_file(file_input1: str, path_database: str) -> True | False:
    file_input1 = file_input1.strip().upper()
    return os.path.exists(get_file_path(path_database, file_input=file_input1, extension="csv"))

def get_unique_filename(files: list) -> str:
    while True:
        file_input = input("What is the file name (case sensitive): ").upper()
        if file_input not in files:
            files.append(file_input)
            return file_input
        print("This file already exists in the portfolio. Please choose another file.")
        continue

def get_file_path(os_path: str, file_input: str, extension: str = "csv") -> str:
    extension = extension.strip().lower()
    if extension == "csv":
        file_name_with_ext = f"{file_input}.csv"
    elif extension == "xlsx":
        file_name_with_ext = f"{file_input}.xlsx"
    else:
        raise ValueError("Unsupported file extension. Supported extensions are 'csv' and 'xlsx'.")
    file_path = os.path.join(os_path, file_name_with_ext)
    return file_path

def read_file(file_path: str) -> DataFrame:
    file_read = read_csv(file_path, index_col=False)
    df_file_read = DataFrame(file_read)
    df_file_read.index += 1
    return df_file_read

def get_valid_weight(file, weights: list, elements_number: int, current_index: int) -> float:
    if current_index == elements_number - 1:
        remaining_weight = round(1 - sum(weights), 2)
        print(f"\n\n===> Assigning remaining weight of {remaining_weight} to {file}.")
        return remaining_weight
    remaining_stocks = elements_number - len(weights)
    while True:
        weight = get_percentage(f"Weight of {file}: ")
        total_weight = round(sum(weights) + weight, 2)
        if total_weight >= 1:
            print(f"The last {remaining_stocks} stocks in the portfolio cannot have 0.00 percent.")
            print("Please try again.")
            continue
        return weight

def set_date(closing: dict, df_file_read: DataFrame, index: int) -> dict:
    if index in [0, 1]:
        try:
            closing["Date"] = to_datetime(df_file_read["Date"]).dt.date
            return closing
        except KeyError:
            return False
    return closing

def set_closing_prices(closing: Union[dict, DataFrame], df_file_read: DataFrame,
                       file_input: str, column_name: str = "Adj Close") -> DataFrame:
    try:
        df_file_read[column_name] = to_numeric(df_file_read[column_name])
        if isinstance(closing, dict):
            closing[file_input] = df_file_read[column_name]
            closing_df = DataFrame(closing)
        elif isinstance(closing, DataFrame):
            closing[file_input] = df_file_read[column_name]
            closing_df = closing
        else:
            raise TypeError("The 'closing' variable is not a dictionary or a DataFrame.")
    except KeyError:
        print(f"Column '{column_name}' not found in the data.")
    except Exception as e:
        print(f"Error setting closing prices for {file_input}: {e}")
    return closing_df

def prepare_closing_df(closing_df: DataFrame)-> DataFrame:

    try:
        closing_df.set_index("Date", inplace=True)
        closing_df.dropna(inplace=True)
    except Exception as e:
        raise RuntimeError(f"Error indexing Date or dropping NaN: {e}")
    return closing_df


def save_data(closing_df: DataFrame,
               df_correlation: DataFrame,
               df_portfolio: DataFrame,
               path_saving_folder: str,
               df_sector_DL0: DataFrame) -> None:
    print("\n\nSave file options:")
    print("1) Excel")
    print("2) CSV")
    while True:
        mode = get_int_positive("Option: ")
        if mode == 1:
            save_excel(closing_df, df_correlation, df_portfolio, path_saving_folder, df_sector_DL0)
            break
        elif mode == 2:
            save_csv(closing_df, df_correlation, df_portfolio, path_saving_folder, df_sector_DL0)
            break
        else:
            print("Choose a correct option.")
            continue

def save_excel(closing_df: DataFrame,
                df_correlation: DataFrame,
                df_portfolio: DataFrame,
                path_saving_folder: str,
                df_sector_DL0: DataFrame) -> None:
    try:
        pathf = get_file_path(path_saving_folder, "Portfolio_Analysis", extension="xlsx")
    except Exception as e:
        raise e("Error")
    while True:
        try:
            with ExcelWriter(pathf) as writer:
                closing_df.to_excel(writer, sheet_name='Daily return')
                df_sector_DL0.to_excel(writer, sheet_name='Market_return')
                df_correlation.to_excel(writer, sheet_name='Correlation')
                df_portfolio.to_excel(writer, sheet_name='Recap')
                break
        except RuntimeError:
            pathf = get_file_path(path_saving_folder, "Portfolio_Analysis-alt", extension="xlsx")
            print("Error: File might be opened somewhere, we are trying the alternative path.")
            continue
        except Exception as e:
            raise OSError(f"Error saving Excel file: {e}")

def save_csv(closing_df: DataFrame,
             df_correlation: DataFrame,
             df_portfolio: DataFrame,
             path_saving_folder: str,
             df_sector_DL0: DataFrame) -> None:
    try:
        path = get_file_path(path_saving_folder, "Portfolio_Analysis", extension="csv")
        closing_df.to_csv(path, mode="w")
        df_correlation.to_csv(path, mode="a")
        df_portfolio.to_csv(path, mode="a")
        df_sector_DL0.to_csv(path, mode="a")
        print("The file has been successfully saved.")
    except Exception as e:
        raise OSError(f"Error saving CSV file: {e}")