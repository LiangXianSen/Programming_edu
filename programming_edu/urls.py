"""programming_edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.static import serve
import xadmin
from users.views import IndexView, LoginView
from programming_edu.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #跳转index
    url(r'^$', IndexView.as_view(), name='index'),
    #login
    url(r'^login/$', LoginView.as_view(), name='login'),
    # login
    url(r'^register/$', LoginView.as_view(), name='register'),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),

    #课程相关URL配置
    url(r'^course/', include(('courses.urls', 'courses'), namespace="course")),
    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]
