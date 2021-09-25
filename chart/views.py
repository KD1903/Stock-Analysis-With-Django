from django.shortcuts import render
import datetime as dt

from .dataset import DataSet

# Create your views here.
# def chartdata(request):
#     price = priceData()
#     context = {
#         'tsla': price[0],
#         'aapl': price[1],
#         'goog': price[2],
#         'fb': price[3],
#         'doge': price[4],
#         'btc': price[5]
#     }
#     return render(request, 'home.html', context)

def stockdata(request):
    print(request.POST['token'])
    token = request.POST['token'].upper()

    data = DataSet(token)
    # data = [current price, highest, lowest, plot]

    context = {
        'current': data[0],
        'highest': data[1],
        'lowest': data[2],
        'plt': data[3],
    }

    return render(request, 'chart.html', context)

def dashboard(request):
    # token = request.POST['token'].upper()

    data = DataSet('AAPL')

    # context = {
    #     'range': range(30),
    #     'date': data[0],
    #     'open': data[1],
    #     'close': data[2],
    #     'high': data[3],
    #     'low': data[4],
    #     'plt': data[5],
    # }

    context = {
        'dataset': data[0],
        'plt': data[1],
    }

    return render(request, 'index.html', context)