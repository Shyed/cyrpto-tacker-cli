# Import request library for API calls
import requests

# CoinGecko API endpoint
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Function to get crypto price
def get_price(crypto_id):
    params = {
        "ids": crypto_id,                     # Cryptocurrency name (bitcoin, ethereum)
        "vs_currencies": "usd"                # Convert price to USD
    }

    try:
        print("Fetching price...")            # Show loading message

        # Send GET request to API
        response = requests.get(API_URL, params=params)
        
        # Convert response to JSON
        data = response.json()

        # Check if crypto exist in response
        if crypto_id in data:
            return data[crypto_id]["usd"]
        else:
            return None

    # Handle errors (network issues, invalid response, etc. )
    except Exception as e:
        print("Error:", e)
        return None

# Main program execution
if __name__ == "__main__":
    print("=== Crypto Tracker ===")              # App tile: Always shows on start
    print("Available coins: bitcoin, ethereum")

    # Get user input
    coin = input("Enter the cryptocurrency name (e.g. bitcoin): ").strip().lower()
    
    # Fetch price
    price = get_price(coin)

    if price is not None:
        # Display formatted price
        print(f"\nCurrent {coin.upper()} price: ${price:.2f} USD")
    else:
        # Handle invalid coin input
        print(f"Price not found for '{coin}'. Make sure it's supported by CoinGecko.")
