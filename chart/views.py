from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import datetime as dt

from .dataset import DataSet
from authUser.models import Profile
from django.contrib.auth.models import User

def stockdata(request):
    print(request.POST['token'])
    token = request.POST['token'].upper()

    data = DataSet(token)
    # data = [current price, highest, lowest, plot]

    context = {
        'current': data[1],
        'highest': data[2],
        'lowest': data[3],
        'plt': data[4],
    }

    return render(request, 'chart.html', context)

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        user_obj = User.objects.filter(username = username).first()
        
        obj = Profile.objects.get(user=user_obj)
        tokens = obj.tokens
        
        tokens = list(tokens.split(','))

        if '' in tokens:
            tokens.remove('')

    if request.method == 'POST':
        tkn = request.POST['token']
        
    else:
        tkn = 'AAPL'

    data = DataSet(tkn)

    context = {
        'dataset': data[0],
        'current': data[1],
        'high': data[2],
        'low': data[3],
        'plt': data[4],
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
        tokens.add(token.upper())
        
        if '' in tokens:
            tokens.remove('')

        add_tokens = ','.join(tokens)
        obj.tokens = add_tokens
        obj.save()

    data = DataSet(token)
    
    context = {
        'dataset': data[0],
        'current': data[1],
        'high': data[2],
        'low': data[3],
        'plt': data[4],
        'username': username,
        'tokens': tokens,
        'tkn': token,
    }

    return render(request, 'index.html', context)

def remove_token(request):
    token = request.POST['new_token']

    if request.user.is_authenticated:
        username = request.user.username
        user_obj = User.objects.filter(username = username).first()
        
        obj = Profile.objects.get(user=user_obj)
        
        tokens = set(obj.tokens.split(','))
        if token in tokens:
            tokens.remove(token)
        
        if '' in tokens:
            tokens.remove('')

        add_tokens = ','.join(tokens)
        obj.tokens = add_tokens
        obj.save()

    data = DataSet(token)
    
    context = {
        'dataset': data[0],
        'current': data[1],
        'high': data[2],
        'low': data[3],
        'plt': data[4],
        'username': username,
        'tokens': tokens,
        'tkn': token,
    }

    return render(request, 'index.html', context)