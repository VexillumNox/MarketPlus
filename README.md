# MarketPlus

**MarketPlus** is a web application built with Flask that allows users to view real-time stock market data. Users can search for a stock symbol (e.g., `AAPL` for Apple) and see the latest stock information pulled from the Alpha Vantage API. The project is designed to be simple, lightweight, and easy to use.

---

## Features

- Real-time stock data retrieval  
- Stock search feature by symbol (e.g., `AAPL`, `TSLA`)  
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
```

### 2. Set up a virtual environment

**On macOS/Linux:**

```bash
python3 -m venv myenv
source myenv/bin/activate
```

**On Windows (PC):**

```bash
python -m venv myenv
myenv\Scripts\activate
```

> If you see an error like `'python' is not recognized`, try using `python3` instead of `python`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of your project directory and add your Alpha Vantage API key:

```
API_KEY=your_alphavantage_api_key
```

**On Windows using PowerShell:**

```powershell
New-Item -Path . -Name ".env" -ItemType "file"
```

Then edit the file using Notepad or your code editor.

### 5. Run the application

**On macOS/Linux or Windows:**

```bash
python run.py
```

Once running, the app will be available at:

```
http://127.0.0.1:5000/
```

---

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`
2. Enter a stock symbol such as `AAPL` or `TSLA` into the search bar
3. View the returned real-time stock data including prices, trends, and timestamps

---

## Troubleshooting

### 429 Too Many Requests

If you receive the error `429 Too Many Requests`, it means you're hitting the rate limit of the free-tier Alpha Vantage API. You can either:

- Wait for the rate limit to reset (usually after 1 minute)
- Consider upgrading your Alpha Vantage plan for higher request limits

> For further details, check the [Alpha Vantage API rate limits](https://www.alphavantage.co/support/#api-key)

---

## Contributing

Contributions are welcome.

### How to Contribute

1. Fork the repository on GitHub
2. Clone your fork to your local machine:

```bash
git clone https://github.com/yourusername/MarketPlus.git
cd MarketPlus
```

3. Create a new branch:

```bash
git checkout -b feature-branch
```

4. Make your changes
5. Commit your changes:

```bash
git commit -m "Add new feature"
```

6. Push to your fork:

```bash
git push origin feature-branch
```

7. Open a pull request to the main branch of this repository

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support:

**Adam** — niemi1as@gmail.com
