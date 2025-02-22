import requests  # For API calls
import time     # For delays between updates

# Function to fetch Bitcoin price
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]
        return price
    except Exception as e:
        return f"Error fetching price: {e}"

# Main loop to display price every 10 seconds
def track_bitcoin():
    print("Bitcoin Price Tracker - Ctrl+C to stop")
    while True:
        price = get_bitcoin_price()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Bitcoin Price: ${price}")
        time.sleep(10)  # Wait 10 seconds before next update

# Run the tracker
if __name__ == "__main__":
    track_bitcoin()