from flask import Flask, render_template, request
from flask_caching import Cache
import logging
import os
import requests

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the API key from environment variable
API_KEY = os.getenv("YTW957VZ1HRVA6HH")  # Ensure the environment variable is set
API_BASE_URL = "https://www.alphavantage.co/query"

app = Flask(__name__)

# Configuring Flask-Caching
app.config['CACHE_TYPE'] = 'filesystem'
app.config['CACHE_DIR'] = './cache'  # Cache files will be stored in a folder named 'cache'

cache = Cache(app)

def get_stock_data(symbol):
    url = f"{API_BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    
    logging.debug(f"Fetching data for symbol: {symbol}")
    
    response = requests.get(url)
    
    logging.debug(f"Response Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()

        logging.debug(f"API Response: {data}")  # Log the entire response for troubleshooting

        if "Error Message" in data:
            logging.error(f"API Error: {data['Error Message']}")
            return {"error": "API Error: " + data["Error Message"]}
        if "Note" in data:
            logging.error("API Rate Limit Exceeded")
            return {"error": "API Rate Limit Exceeded"}
        
        stock_data = data.get("Time Series (5min)", {})
        if not stock_data:
            logging.warning(f"No data available for symbol {symbol}.")
            return {"error": "No data available for symbol."}
        
        return stock_data
    else:
        logging.error(f"HTTP Error: {response.status_code}")
        return {"error": f"HTTP Error: {response.status_code}"}

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None  # Default to None for no data
    
    if request.method == "POST":
        symbol = request.form["symbol"]

        # Try to fetch the data from cache first
        cached_data = cache.get(symbol)

        if cached_data is None:
            # If no cached data, fetch it from the API
            stock_data = get_stock_data(symbol)

            if "error" in stock_data:
                # If there's an error, log it
                logging.error(f"Error fetching stock data: {stock_data['error']}")
            else:
                # Cache the data for 10 minutes
                cache.set(symbol, stock_data, timeout=600)  # Cache for 10 minutes
        else:
            # Use cached data
            stock_data = cached_data

        logging.debug(f"Stock Data: {stock_data}")  # Log the stock data
        return render_template("index.html", stock_data=stock_data)
    
    return render_template("index.html", stock_data=stock_data)

if __name__ == "__main__":
    app.run(debug=True)
