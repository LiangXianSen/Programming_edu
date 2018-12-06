#  COURSE
+ /urls.py
```python
from django.conf.urls import url, include

urlpatterns = [
    #课程相关URL配置
    url(r'^course/', include(('courses.urls', 'courses'), namespace="course")),
  ]

```
+ /courses/urls.py
```python
# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/12/5 12:34'

from django.conf.urls import url, include

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
]
```

+ course-list.html
```html

```
+ course-detail.html
```html

```

+ course-view.py
```python

```