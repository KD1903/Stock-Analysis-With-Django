from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import datetime as dt

from .dataset import DataSet
from authUser.models import Profile
from django.contrib.auth.models import User

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

@login_required(login_url='/')
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        user_obj = User.objects.filter(username = username).first()
        
        obj = Profile.objects.get(user=user_obj)
        tokens = obj.tokens
        
        tokens = list(tokens.split(','))

    if request.method == 'POST':
        tkn = request.POST['token']
        
    else:
        tkn = 'AAPL'

    data = DataSet(tkn)

    context = {
        'dataset': data[0],
        'plt': data[1],
        'username': username,
        'tokens': tokens,
        'tkn': tkn,
    }

    return render(request, 'index.html', context)

def add_token(request):
    token = request.POST['new_token']

    if request.user.is_authenticated:
        username = request.user.username
        user_obj = User.objects.filter(username = username).first()
        
        obj = Profile.objects.get(user=user_obj)
        
        tokens = set(obj.tokens.split(','))
        tokens.add(token)

        tokens = ','.join(tokens)
        obj.tokens = tokens
        obj.save()

    data = DataSet(token)
    
    context = {
        'dataset': data[0],
        'plt': data[1],
        'username': username,
        'tokens': list(tokens.split(',')),
        'tkn': token,
    }

    return render(request, 'index.html', context)