#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

from django.shortcuts import  redirect,render,HttpResponse
from app.forms.hosts import HostModelForms
from rbac.services.Menu_urls import  memory_reverse

# 数据库操作
from app import models

def host_list(request):
    host_queryset = models.Host.objects.all()
    return render(request,'host_list.html',{'host_list':host_queryset})

def host_add(request):
    """
    添加主机
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = HostModelForms()
        return render(request, 'rbac/change.html', {'form': form})

    form = HostModelForms(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/change.html', {'form': form})

def host_edit(request,pk):
    obj = models.Host.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('主机不存在')
    if request.method == 'GET':
        form = HostModelForms(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})

    form = HostModelForms(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/change.html', {'form': form})

def host_del(request,pk):
    origin_url = memory_reverse(request, 'host_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': origin_url})

    models.Host.objects.filter(id=pk).delete()
    return redirect(origin_url)