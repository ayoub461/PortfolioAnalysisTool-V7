import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Nasdaq historical data page
url = "https://www.nasdaq.com/market-activity/quotes/historical"

# Send a GET request to the website
response = requests.get(url)
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data (example for table rows, adjust selectors as needed)
    # You will need to inspect the website to find the correct tags and classes
    table = soup.find('table')
    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')
    
    data = []
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)
