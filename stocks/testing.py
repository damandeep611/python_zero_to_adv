import yfinance as yf 
import plotly.graph_objs as go 

ticker = 'RELIANCE.NS'
data = yf.download(ticker, start='2023-01-01', end='2024-05-15')
 

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='close price'))

fig.update_layout(title='historical close prices for' + ticker, xaxis_title='Date', yaxis_title='Price(INR)', template='plotly_dark')

fig.show()
