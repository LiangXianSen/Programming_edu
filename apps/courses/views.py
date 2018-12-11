# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/12/5 12:34'

from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import View
from django.db.models import Q


from .models import Course, Chapter, CourseResource
from operation.models import CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin
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

        pagi = Paginator(all_courses, 3, request=request)

        courses = pagi.page(pagenum)

        return render(request, 'course-list.html', {
            "all_courses":courses,
            "sort":sort,
            "hot_courses":hot_courses
        })


class CourseDetailView(View):
    """
    course details
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        return render(request, 'course-detail.html', {
            "course":course,
        })


class ChapterInfoView(View):
    """
    Chapter detials
    """
    def get(self, request, chapter_id):
        chapter = Chapter.objects.get(id=int(chapter_id))
        video = chapter.get_chapter_video()

        return render(request, 'chapter-detail.html', {
            "chapter": chapter,
        })


class CommentsView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course).order_by("-id")
        return render(request, "course-comment.html", {
            "course":course,
            "course_resources":all_resources,
            "all_comments":all_comments

        })


class AddCommentsView(View):
    """
    用户添加课程评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if int(course_id) >0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')
