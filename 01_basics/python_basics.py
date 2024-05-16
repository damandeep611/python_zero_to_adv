import yfinance as yf 


ticker = 'RELIANCE.NS'
data = yf.download(ticker, start='2024-05-14', end='2024-05-15')
print(data.head())
