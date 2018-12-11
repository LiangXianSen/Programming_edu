# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/11/30 9:37'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile


class BaseSetting(object):
    """
    xadmin 全站主题配置
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "TM_EDU后台管理系统"
    site_footer = "TM_EDU"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
