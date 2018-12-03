# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/12/3 11:09'

from django import forms

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
