import json

from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse

from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


def login(request):
    result = {'status': False, 'message': None}
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        # login data
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # authentication
        # TODO(Kevin): only allowed retry three times at most
        user = auth.authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)  # set user login, keep session
                result['status'] = True
        else:
            login_form.add_error('password', "用户名或密码错误")
    error_str = login_form.errors.as_json()
    result['message'] = json.loads(error_str)
    return HttpResponse(json.dumps(result))


def logout(request):
    if request.user:
        auth.logout(request)
    return redirect("/")


def register(request):
    result = {'status': False, 'message': None}
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        phone = request.POST['phone']
        email = request.POST['email']
        if password == repassword:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password, phone=phone, email=email)
                result['status'] = True
            else:
                register_form.add_error('username', "用户已存在")
        else:
            register_form.add_error('repassword', "两次输入的密码不一致")
    error_str = register_form.errors.as_json()
    result['message'] = json.loads(error_str)
    return HttpResponse(json.dumps(result))

