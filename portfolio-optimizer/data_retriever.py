import pandas as pd

"""
Data Retrieval Module for Portfolio Optimization

Purpose:
    Retrieves stock tickers from CSV files organized by sector for portfolio analysis.

Required Data Structure:
    - CSV files must be named as '{sector}-tick.csv'
    - Each CSV should have tickers listed in columns
    - Files should be organized by sector in a single folder
    - This is an example of how I used it to get data from a csv

Example Directory Structure:
    your_folder/
    ├── finance-tick.csv
    ├── tech-tick.csv
    ├── industrial-tick.csv
    └── energy-tick.csv
"""

def retrieve_tickers():
    # List of sectors to process - must match CSV file names (without -tick.csv)
    sectors = ["finance", "tech", "industrial", "energy"]
    
    # Dictionary to store tickers for each sector
    sectors_tickers = {}
    
    # Iterate through each sector to read its corresponding CSV
    for i in range(len(sectors)):
        # Read CSV file for current sector
        csv_data = pd.read_csv(f"/your_folder/{sectors[i]}-tick.csv")
        current_sector = sectors[i]  # Store sector name for clarity
        
        # Extract ticker column and update dictionary
        # Note: Column name must match exactly as shown
        sectors_tickers.update({
            current_sector: csv_data["Index Holdings and weightings as of x PM ET DATE"]
        })
        
        # Convert pandas Series to list for easier manipulation
        sectors_tickers[current_sector] = sectors_tickers[current_sector].tolist()
        
        # Remove header row that contains "SYMBOL"
        if sectors_tickers[current_sector][0] == "SYMBOL" or "symbol":
            del sectors_tickers[current_sector][0]
    
    return sectors_tickers

# set to "True" to print retrieved tickers for verification
check = False
if check:
    print(retrieve_tickers())