from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import File

from django.conf import settings

import os


def index(request):
    context = {}
    try:
        files = File.objects.all()
        context["files"] = files
    except Exception as err:
        raise Http404(err)
    return render(request, "store/index.html", context=context)

