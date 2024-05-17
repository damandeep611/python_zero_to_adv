class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def total_value(self):
        return sum(stock.price for stock in self.stocks)

# Usage
portfolio = Portfolio()
portfolio.add_stock(Stock('AAPL', 150.25))
portfolio.add_stock(Stock('GOOGL', 2800.75))
print(f"Total portfolio value: ${portfolio.total_value()}")
