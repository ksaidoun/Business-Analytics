from yahooquery import Ticker
import csv

# Open the CSV file
with open('salaries_clean.csv', encoding='utf-8', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    
    # Initialize an empty array to store the Ticker values
    tickers = []
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the value from the Ticker column and append it to the tickers array
        tickers.append(row['Ticker'])
        
        
# Open the output file in write mode
with open('data_profits.csv', 'w') as f:
    # Loop through each ticker and retrieve the profit
    for ticker in tickers:
        if (ticker == ''):
            print("", file=f)
            continue

        try:
            # Create a Ticker object for the current ticker
            stock = Ticker(ticker)
            
            # Retrieve the income statement for the current ticker
            gross_profit = stock.income_statement().get('GrossProfit')[0]

            
            # Print the profit for the current ticker
            print(str(gross_profit), file=f)
        except:
            print("Failed on " + ticker, file=f)
            