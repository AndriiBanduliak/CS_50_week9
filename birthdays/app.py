# application.py

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Sample user portfolio data for testing
sample_portfolio = [
    {'symbol': 'AAPL', 'shares': 10},
    {'symbol': 'GOOGL', 'shares': 5},
    {'symbol': 'MSFT', 'shares': 8}
]

@app.route('/')
def index():
    # TODO: Replace sample_portfolio with actual database query to get user's portfolio
    portfolio = sample_portfolio

    # Retrieve the user's cash balance from the database
    # TODO: Replace cash_balance with actual database query
    cash_balance = 5000

    # Calculate the total value of each holding (shares times price)
    for stock in portfolio:
        symbol = stock['symbol']
        price = lookup(symbol)
        if price is not None:
            stock['price'] = price
            stock['total_value'] = price * stock['shares']
        else:
            stock['price'] = 'N/A'
            stock['total_value'] = 'N/A'

    # Calculate the total value of all holdings (stocks' total value plus cash)
    total_value = cash_balance + sum(stock['total_value'] for stock in portfolio)

    return render_template('index.html', portfolio=portfolio, cash=cash_balance, total_value=total_value)

# Define the lookup function to get stock price
def lookup(symbol):
    # Make an API call to get stock data
    # TODO: Replace 'https://api.example.com/stock/{symbol}' with actual API endpoint
    response = requests.get(f'https://api.example.com/stock/{symbol}')
    data = response.json()

    # Check if the stock symbol was found
    if 'price' in data:
        return data['price']
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
