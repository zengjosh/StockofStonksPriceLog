import os
import requests
import csv
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file if running locally
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('HYPIXEL_API_KEY')

# Fetch data from the Hypixel API
def fetch_data():
    url = f"https://api.hypixel.net/skyblock/bazaar?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Log data to a CSV file
def log_data():
    data = fetch_data()
    if data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Extract specific data, e.g., price of Polished Pumpkin
        polished_pumpkin = data['products']['STOCK_OF_STONKS']['quick_status']
        buy_price = polished_pumpkin['buyPrice']
        sell_price = polished_pumpkin['sellPrice']

        with open('STOCK_OF_STONKS_price_history.csv', 'a', newline='') as csvfile:
            fieldnames = ['timestamp', 'item', 'buy_price', 'sell_price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            print(f"Logged data for {'STOCK_OF_STONKS'} at {timestamp}")
            
            # Write header only if the file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            
            writer.writerow({
                'timestamp': timestamp,
                'item': 'STOCK_OF_STONKS',
                'buy_price': buy_price,
                'sell_price': sell_price
            })

if __name__ == "__main__":
    log_data()
