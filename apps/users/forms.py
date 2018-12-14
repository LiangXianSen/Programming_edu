from django import forms
from django.core.exceptions import ValidationError


# 自己写一个验证规则函数
def mobile_validate(value):
    import re
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(required=True, min_length=6, max_length=12,
                               error_messages={'required': '密码不能为空', 'min_length': '最少6位', 'max_length': '最多12位'})


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(required=True, min_length=6, max_length=12,
                               error_messages={'required': '密码不能为空', 'min_length': '最少6位', 'max_length': '最多12位'})
    repassword = forms.CharField(required=True, min_length=6, max_length=12,
                               error_messages={'required': '密码不能为空', 'min_length': '最少6位', 'max_length': '最多12位'})
    phone = forms.CharField(required=True, validators=[mobile_validate, ], error_messages={'required': '手机号不能为空'})
    email = forms.EmailField(required=True, error_messages={'required': 'email不能为空', 'invalid': '请输入邮箱格式'})