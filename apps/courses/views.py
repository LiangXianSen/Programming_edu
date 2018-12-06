# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/12/5 12:34'

from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import View
from django.db.models import Q

from .models import Course
# Create your views here.


class CourseListView(View):

    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        hot_courses = Course.objects.all().order_by("-click_nums")[0:3]

        #filter index course
        search_keywords = request.GET.get('keywords', "")

        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        #order
        sort = request.GET.get("sort", "")

        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            if sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        #pagenation
        try:
            pagenum = request.GET.get("page", 1)
        except PageNotAnInteger:
            pagenum = 1

        pagi = Paginator(all_courses, 6, request=request)

        courses = pagi.page(pagenum)

        return render(request, 'course-list.html', {
            "all_courses":courses,
            "sort":sort,
            "hot_courses":hot_courses
        })


class CourseDetailView(View):
    pass


class CourseInfoView(View):
    pass


class CommentsView(View):
    pass


class AddCommentsView(View):
    pass