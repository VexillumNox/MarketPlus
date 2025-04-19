# MarketPlus

**MarketPlus** is a web application built with Flask that allows users to view real-time stock market data. Users can search for a stock symbol (e.g. `AAPL` for Apple) and see the latest stock information pulled from the Polygon.io API. The project is designed to be simple, lightweight, and easy to use.

---

## Features

- Real-time stock data retrieval  
- Stock search feature by symbol (e.g. `AAPL`, `TSLA`)  
- Simple, user-friendly web interface  
- Integration with a **free** Polygon.io API for live data  
- Runs locally or remotely using services like Ngrok  

---

## Technologies

- Python 3.x  
- Flask (web framework)  
- Polygon.io API  
- HTML / CSS / JavaScript (frontend)  

---

## Installation

### 1. Clone the repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/yourusername/MarketPlus.git
cd MarketPlus
```

### 2. Set up a virtual environment

#### On macOS/Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### On Windows (PC):

```bash
python -m venv myenv
myenv\Scripts\activate
```

If you see an error like `'python' is not recognized`, try using `python3` instead of `python`.

### 3. Install dependencies

Once the virtual environment is activated, run:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, you can create it using:

```bash
pip freeze > requirements.txt
```

**Example contents of `requirements.txt`:**

```
Flask
polygon-api-client
requests
```

### 4. Set up environment variables

Create a `.env` file in the root of your project directory and add your **free** Polygon.io API key like this:

```
API_KEY=your_polygon_api_key
```

If you're on Windows and using PowerShell, you can create the file like this:

```powershell
New-Item -Path . -Name ".env" -ItemType "file"
```

Then edit it using Notepad or your code editor.

### 5. Run the application

#### On macOS/Linux:

```bash
python run.py
```

#### On Windows (PC):

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

**429 Too Many Requests**

This means you're hitting the rate limit of the free-tier Polygon.io API. You can either wait for the limit to reset or upgrade your Polygon.io plan for more requests.

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

7. Open a pull request to the `main` branch of this repository

---

## License

This project is licensed under the [MIT License](LICENSE)

---

## Contact

For questions or support:

**Adam** — [niemi1as@gmail.com](mailto:niemi1as@gmail.com)
