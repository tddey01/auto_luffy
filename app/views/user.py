#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from app import models
from app.forms.users import UserModelForms,UpdateUserModelForms ,ResetPasswordUserModelForms
from rbac.services.Menu_urls import memory_reverse


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """

    user_queryset = models.UserInfo.objects.all()

    return render(request, 'user_list.html', {'user_queryset': user_queryset})


def user_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UserModelForms()
        return render(request, 'rbac/change.html', {'form': form})

    form = UserModelForms(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'user_list'))

    return render(request, 'rbac/change.html', {'form': form})


def user_edit(request, pk):
    """
    编辑用户
    :param request:
    :param pk: 要修改的用户ID
    :return:
    """
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    if request.method == 'GET':
        form = UpdateUserModelForms(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})

    form = UpdateUserModelForms(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'user_list'))

    return render(request, 'rbac/change.html', {'form': form})


def user_reset_password(request, pk):
    """
    重置密码
    :param request:
    :param pk:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('用户不存在')
    if request.method == 'GET':
        form = ResetPasswordUserModelForms()
        return render(request, 'rbac/change.html', {'form': form})

    form = ResetPasswordUserModelForms(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'user_list'))

    return render(request, 'rbac/change.html', {'form': form})


def user_del(request, pk):
    """
    删除用户
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request, 'user_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': origin_url})

    models.UserInfo.objects.filter(id=pk).delete()
    return redirect(origin_url)
