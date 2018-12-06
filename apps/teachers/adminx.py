# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/11/30 10:18'

import xadmin

from .models import Teacher


class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company']
    search_fields = ['name', 'work_years', 'work_company']
    list_filter = ['name', 'work_years', 'work_company']
    model_icon = 'fa fa-user-md'


xadmin.site.register(Teacher, TeacherAdmin)
