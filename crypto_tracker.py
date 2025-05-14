import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_price(crypto_id):
    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }

    try:
        print("Fetching price...")  # Ensures output appears
        response = requests.get(API_URL, params=params)
        data = response.json()

        if crypto_id in data:
            return data[crypto_id]["usd"]
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    print("=== Crypto Tracker ===")  # Always shows on start
    print("Available coins: bitcoin, ethereum")

    coin = input("Enter the cryptocurrency name (e.g. bitcoin): ").strip().lower()
    price = get_price(coin)

    if price is not None:
        print(f"\nCurrent {coin.upper()} price: ${price:.2f} USD")
    else:
        print(f"Price not found for '{coin}'. Make sure it's supported by CoinGecko.")
