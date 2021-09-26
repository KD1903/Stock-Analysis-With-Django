from plotly.offline import plot
import plotly.graph_objs as go
import datetime as dt
import yfinance as yf

def DataSet(token): 

    # data = web.DataReader(token, 'yahoo', start, end, interval='1m')
    data = yf.download(token.upper(), period='1y')

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

    plot_div = plot({'data': fig}, 
                    output_type='div')

    my_formater = "{0:.2f}"

    current = my_formater.format(data['Close'][-1])
    high = my_formater.format(data['High'].max())
    low = my_formater.format(data['Low'].min())

    # data.index.to_datetime()

    date_data = list(data.index[-30:])
    volume_data = list(data['Volume'].tail(30))
    price_data = list(data['Adj Close'].tail(30))
    open_data = list(data['Open'].tail(30))
    close_data = list(data['Close'].tail(30))
    high_data = list(data['High'].tail(30))
    low_data = list(data['Low'].tail(30))

    date_data = [d.strftime('%d %b %Y') for d in date_data]
    volume_data = ["{0:.0f}".format(i) for i in volume_data]
    price_data = [my_formater.format(i) for i in price_data]
    open_data = [my_formater.format(i) for i in open_data]
    close_data = [my_formater.format(i) for i in close_data]
    high_data = [my_formater.format(i) for i in high_data]
    low_data = [my_formater.format(i) for i in low_data]

    date_data.reverse()
    volume_data.reverse()
    price_data.reverse()
    open_data.reverse()
    close_data.reverse()
    high_data.reverse()
    low_data.reverse()

    dataset = zip(
        date_data,
        volume_data,
        price_data,
        open_data,
        close_data,
        high_data,
        low_data,
    )

    data_return = [dataset, current, high, low, plot_div]

    return data_return