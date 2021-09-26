"""stockAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chart.views import *
from authUser.views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('stock/', stockdata),
    path('admin/', admin.site.urls),

    path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    path('token/', token, name='token'),
    path('sucessful/', sucessful, name='sucessful'),
    path('verify/<auth_token>', verify, name='verify'),
    path('error/', error, name='error'),
    path('add_token/', add_token, name='add_token'),
    path('remove_token/', remove_token, name='remove_token'),
    path('logout_user/', logout_user, name='logout_user'),

    path('dashboard/', dashboard, name='dashboard'),
]
