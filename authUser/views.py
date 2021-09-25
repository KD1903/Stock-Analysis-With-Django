from django.shortcuts import render, HttpResponse, redirect

import datetime as dt
import yfinance as yf

import uuid
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout

from authUser.models import Profile

# Create your views here.
def user_login(request):
    
    if request.method == 'POST': 
        username = request.POST.get('username')
        
        password = request.POST.get('password')

        user_obj=User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request,'User Not Found')
            return redirect('login')

        profile_obj = Profile.objects.filter(user = user_obj ).first()
        if not profile_obj.is_varified:
            messages.success(request,'Check your email to varify your account')
            return redirect('login')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong credentials')
            return redirect('login')

        login(request, user)
        return redirect('dashboard/')

    my_formater = "{0:.2f}"

    data = []
    token = ['TSLA', 'AAPL', 'GOOG', 'FB', 'DOGE-INR', 'BTC-USD']

    for tkn in token:
        webData = yf.download(tkn, period='3d')
        data.append(my_formater.format(webData['Close'][-1]))
    
    context = {
        'tsla': data[0],
        'aapl': data[1],
        'goog': data[2],
        'fb': data[3],
        'doge': data[4],
        'btc': data[5]
    }

    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username already registered')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email already registered')
                return redirect('/register')

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())

            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()

            send_mail_varification(email, auth_token)

            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request, 'register.html')

def send_mail_varification(email, token):
    subject = 'varify your account'
    message = f'click on this link verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]

    send_mail(subject, message, email_from, recipient)

def token(request):
    return render(request, 'token.html')

def sucessful(request):
    return render(request, 'sucessful.html')


def verify(request,auth_token):
    try:
        profile_obj=Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_varified = True
            profile_obj.save()
            messages.success(request,'Account has been varified')
            return redirect('/')

        else:
            return redirect('/error')
    except Exception as e:
        print(e)


def error(request):
    return render(request,'error.html')