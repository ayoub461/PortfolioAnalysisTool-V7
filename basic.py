import pandas as pd

# Create a date range from January 1, 2020 to December 31, 2020
dates = pd.date_range(start="2020-01-01", end="2020-12-31")

# Create a DataFrame with this date range as the index and a simple column of values
data = {
    "Value": range(len(dates))  # Just an example column with incremental values
}

df = pd.DataFrame(data, index=dates)

print(df)

def days_number(df_cleaned: pd.DataFrame) -> int:
    total_days = (df_cleaned.index[-1] - df_cleaned.index[0]).days
    return total_days

# Test the function with the example DataFrame
print(f"Total days: {days_number(df)}")  # Expected: 365 (because 2020 is a leap year)
