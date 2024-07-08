import os
import csv
from datetime import datetime
from numpy import transpose
import schedule
from neo_api_client import NeoAPI

# Initialize a set to keep track of written instrument tokens globally
written_tokens = set()

# Function to handle incoming messages and append them to the CSV file
def handle_quote(quote):
    # Define the filename with today's date
    filename = "HistoryIntra" + datetime.now().strftime("%d.%m.%Y") + ".csv"
    
    # Check if the file exists and is empty
    file_exists = os.path.isfile(filename)
    is_empty = not os.path.getsize(filename) > 0 if file_exists else False
    
    # Open the CSV file in append mode
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        
        # Write the header if the file is new/empty
        if not file_exists or is_empty:
            writer.writerow(['Time', 'Instrument Token', 'LTP'])
        
        # Append the new quote with the current timestamp
        current_time = datetime.now().strftime("%H:%M:%S")
        instrument_token = quote['instrument_token']       
        ltp = float(quote['ltp'])
        
        # Check if the instrument_token has already been written
        if instrument_token not in written_tokens:
            writer.writerow([current_time, instrument_token, ltp])
            # Add the token to the set
            written_tokens.add(instrument_token)
        else:
            # Only write the time and ltp for already written tokens
            writer.writerow([current_time, ltp])




# Save the response to a text file
#with open("data.txt", "w") as file:
 #   file.write(str(response))

# Define the instrument tokens
instrument_tokens = [{"instrument_token": "13061", "exchange_segment": "nse_cm"},
                     {"instrument_token": "30108", "exchange_segment": "nse_cm"},
                     {"instrument_token": "12531", "exchange_segment": "nse_cm"}
    # ... other instrument tokens ...
]

# Define a wrapper function that fetches the quotes and calls handle_quote with each quote
def job():
    quotes = client.quotes(instrument_tokens=instrument_tokens, quote_type="ltp", isIndex=False)
    for quote in quotes['message']:
        handle_quote(quote)

# Schedule the wrapper function instead of handle_quote directly
schedule.every(0.09).minutes.do(job)

# Subscribe to the instrument tokens for live quotes
client.subscribe(instrument_tokens=instrument_tokens, isIndex=False, isDepth=False)

# Start the schedule loop (this will keep running indefinitely)
while True:
    schedule.run_pending()



