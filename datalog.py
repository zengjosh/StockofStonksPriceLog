import requests
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('HYPIXEL_API_KEY')

def fetch_bazaar_data():
    url = f'https://api.hypixel.net/skyblock/bazaar?key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            return data['products']
        else:
            print('Error in API response:', data['cause'])
            return None
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def log_price_history(item_name, filename='STOCK_OF_STONKS_price_history.csv'):
    bazaar_data = fetch_bazaar_data()
    if bazaar_data and item_name in bazaar_data:
        item_data = bazaar_data[item_name]['quick_status']
        timestamp = datetime.now().isoformat()
        buy_price = item_data['buyPrice']
        sell_price = item_data['sellPrice']
        
        # Write data to CSV
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, item_name, buy_price, sell_price])
        
        print(f"Logged data for {item_name} at {timestamp}")

if __name__ == "__main__":
    item_name = 'STOCK_OF_STONKS'
    log_price_history(item_name)
