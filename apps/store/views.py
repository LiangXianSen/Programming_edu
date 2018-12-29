from django.shortcuts import render, redirect
from django.http import Http404

from django.contrib import messages

from .models import File


def index(request):
    context = {}
    if not request.user.is_authenticated:
        messages.warning(request, '请先登陆')
        return render(request, "store/index.html", context=context)
    try:
        files = File.objects.all()
        context["files"] = files
    except Exception as err:
        raise Http404(err)
    return render(request, "store/index.html", context=context)

