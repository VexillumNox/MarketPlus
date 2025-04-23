# MarketPlus

**MarketPlus** is a web application built with Flask that allows users to view real-time stock market data. Users can search for a stock symbol (e.g. `AAPL` for Apple) and see the latest stock information pulled from the Alpha Vantage API. The project is designed to be simple, lightweight, and easy to use.

---

## Features

- Real-time stock data retrieval  
- Stock search feature by symbol (e.g. `AAPL`, `TSLA`)  
- Simple, user-friendly web interface  
- Integration with a **free** Alpha Vantage API for live data  
- Runs locally or remotely using services like Ngrok  

---

## Technologies

- Python 3.x  
- Flask (web framework)  
- Alpha Vantage API  
- HTML / CSS / JavaScript (frontend)  

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/MarketPlus.git
cd MarketPlus
2. Set up a virtual environment
On macOS/Linux:
bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate
On Windows (PC):
bash
Copy
Edit
python -m venv myenv
myenv\Scripts\activate
If you see an error like 'python' is not recognized, try using python3 instead of python.

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the root of your project directory and add your free Alpha Vantage API key like this:

env
Copy
Edit
API_KEY=your_alphavantage_api_key
If you're on Windows and using PowerShell, you can create the file like this:

powershell
Copy
Edit
New-Item -Path . -Name ".env" -ItemType "file"
Then edit it using Notepad or your code editor.

5. Run the application
On macOS/Linux:
bash
Copy
Edit
python run.py
On Windows (PC):
bash
Copy
Edit
python run.py
Once running, the app will be available at:

cpp
Copy
Edit
http://127.0.0.1:5000/
Usage
Open your web browser and navigate to http://127.0.0.1:5000/

Enter a stock symbol such as AAPL or TSLA into the search bar.

View the returned real-time stock data including prices, trends, and timestamps.

Troubleshooting
429 Too Many Requests

If you receive the error 429 Too Many Requests, it means you're hitting the rate limit of the free-tier Alpha Vantage API. You can either:

Wait for the rate limit to reset (usually after 1 minute).

Consider upgrading your Alpha Vantage plan for higher request limits.

For further details, check the Alpha Vantage API rate limits.

Contributing
Contributions are welcome.

How to Contribute
Fork the repository on GitHub.

Clone your fork to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/MarketPlus.git
cd MarketPlus
Create a new branch:

bash
Copy
Edit
git checkout -b feature-branch
Make your changes.

Commit your changes:

bash
Copy
Edit
git commit -m "Add new feature"
Push to your fork:

bash
Copy
Edit
git push origin feature-branch
Open a pull request to the main branch of this repository.

License
This project is licensed under the MIT License.

Contact
For questions or support:

Adam — niemi1as@gmail.com
