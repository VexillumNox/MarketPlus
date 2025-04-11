from flask import Flask, render_template, request, jsonify
from stock_data import get_stock_data  # Import the function from stock_data.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    error_message = None
    
    if request.method == 'POST':
        symbol = request.form['symbol']
        outputsize = request.form['outputsize']
        
        # Fetch stock data from your stock_data.py function
        stock_data = get_stock_data(symbol, outputsize)

        # If there was an error fetching data, store the error message
        if 'error' in stock_data:
            error_message = stock_data['error']
            stock_data = None

    # Pass stock data (or error message) to the template
    return render_template('index.html', stock_data=stock_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
