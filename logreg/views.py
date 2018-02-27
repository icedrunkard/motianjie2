# coding:utf-8
from django.shortcuts import render_to_response, render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.loader import get_template


# Create your views here.

# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, required=True)
    password = forms.CharField(label='密__码', widget=forms.PasswordInput(), required=True)


# @csrf_protect
# @ensure_csrf_cookie
# @csrf_exempt
def register(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            try:
                User.objects.get(username=username)
                return render_to_response('logreg/share.html', {'registAdd': '已存在', 'username': username})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # user = authenticate(username=username, password=password)
                # auth.login(req, user)
                # 重定向到首页
                # return redirect('/')
                return render(req, 'logreg/share.html', {'registAdd': '注册成功'}, )
    uf=UserForm()
    return render_to_response('logreg/login.html', {'uf': uf}, context_instance=RequestContext(req))


# @csrf_protect
# @ensure_csrf_cookie
# @csrf_exempt
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)  # req.POST 得到的是字典
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 对比提交的数据与数据库中的数据
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                # 比较成功，跳转index
                auth.login(req, user)
                print('*'*20,req.path)
                if 'next' in req.path:
                    next_url = req.path.split('next=')[-1]
                    print(next_url)
                    response = HttpResponseRedirect(next_url)
                else:
                    response = HttpResponseRedirect('/')
                return response

            else:
                return render_to_response('logreg/login.html', context={'login_info': False},
                                          context_instance=RequestContext(req))
    uf = UserForm()
    return render_to_response('logreg/login.html', context={'login_info': True, 'uf': uf},
                              context_instance=RequestContext(req))


# 退出登录
@login_required
def logout(req):
    username = req.user
    auth.logout(req)
    response = HttpResponse('{} has logout!!!'.format(username))
    return response


@login_required
def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render_to_response('logreg/share.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('logreg/share.html', {'uf': uf})
