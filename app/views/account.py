#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from app import models

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    user = request.POST.get('usernaem')
    pwd =  request.POST.get('password')

    models.UserInfo.objects.filter(name=user,password=pwd).first()

def  logout(request):
    pass
