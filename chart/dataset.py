import pandas_datareader as web
from plotly.offline import plot
import plotly.graph_objs as go
import datetime as dt
import yfinance as yf

def DataSet(token): 

    # data = web.DataReader(token, 'yahoo', start, end, interval='1m')
    data = yf.download(token, period='1y')
    print(data)
    # graph = [go.Candlestick(x=data.index, 
    #             open=data['Open'],
    #             high=data['High'],
    #             low=data['Low'],
    #             close=data['Close'], name='market data')]

    fig = go.Figure()

    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    fig.update_layout(
        title=f'{token} live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="7d", step="day", stepmode="backward"),
                dict(count=30, label="30d", step="day", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="todate"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(step="all")
            ])
        )
    )
    
    # layout = {
    #     'title': f'{token} live share price evolution',
    #     'yaxis_title': 'Stock Price (USD per Shares)'
    # }

    plot_div = plot({'data': fig}, 
                    output_type='div')

    my_formater = "{0:.2f}"

    current = my_formater.format(data['Close'][-1])
    high = my_formater.format(data['High'].max())
    low = my_formater.format(data['Low'].min())

    # data = [current price, highest, lowest, plot]
    data = [current, high, low, plot_div]

    return data