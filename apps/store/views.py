from django.shortcuts import render
from django.http import Http404

from .models import File


def index(request):
    context = {}
    try:
        files = File.objects.all()
        context["files"] = files
    except Exception as err:
        raise Http404(err)
    return render(request, "store/index.html", context=context)

