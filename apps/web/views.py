from django.shortcuts import render


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user
    return render(request, "web/index.html", context=context)
