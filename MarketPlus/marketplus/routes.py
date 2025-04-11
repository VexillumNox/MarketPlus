# marketplus/routes.py
from flask import render_template, request
from .stock_data import get_stock_data

def setup_routes(app, cache):
    @app.route("/", methods=["GET", "POST"])
    def index():
        stock_data = None
        error_message = None
        
        if request.method == "POST":
            symbol = request.form.get("symbol")
            outputsize = request.form.get("outputsize", "compact")  # Get the output size from the form
            
            # Check if the stock data is already cached
            stock_data = cache.get(symbol)

            if stock_data is None:
                # If not cached, fetch from API and cache it
                stock_data = get_stock_data(symbol, outputsize)

                # If there's an error with the API response, handle it
                if "error" in stock_data:
                    error_message = stock_data["error"]
                else:
                    cache.set(symbol, stock_data)  # Cache the result for future use

        return render_template("index.html", stock_data=stock_data, error_message=error_message)

    @app.route("/stock_info")
    def stock_info():
        return render_template("stock_info.html")
