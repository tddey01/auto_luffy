"""auto_luffy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from app.views import User_name
from app.views import host_name
from app.views import account
from django.urls import re_path

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^login/$', account.login, name='login'),  # 用户登录页面
    url(r'^logout/$', account.logout, name='logout'),  # 用户注销页面
    # 用户区域
    url(r'^user/list/$', User_name.user_list, name='user_list'),  # 用户列表
    url(r'^user/add/$', User_name.user_add, name='user_add'),  # 添加用户
    url(r'^user/edit/(?P<pk>\d+)/$', User_name.user_edit, name='user_edit'),  # 编辑用户
    url(r'^user/reset/password/(?P<pk>\d+)/$', User_name.user_reset_password, name='user_reset_password'),  # 修改密码用户
    url(r'^user/del/(?P<pk>\d+)/$', User_name.user_del, name='user_del'),  # 删除用户

    # 主机区域
    url(r'^host/list/$', host_name.host_list, name='host_list'),  # 用户列表
    url(r'^host/add/$', host_name.host_add, name='host_add'),  # 添加用户
    url(r'^host/edit/(?P<pk>\d+)/$', host_name.host_edit, name='host_edit'),  # 编辑用户
    url(r'^host/del/(?P<pk>\d+)/$', host_name.host_del, name='host_del'),  # 删除用户
]
