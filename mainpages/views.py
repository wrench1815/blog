from django.shortcuts import render
from .models import ChangelogsModel


def home(request):
    return render(request, 'mainpages/home.html')


def about(request):
    return render(request, 'mainpages/about.html')


def contactMe(request):
    return render(request, 'mainpages/contact_me.html')


def changelogs(request):
    changelogs = ChangelogsModel.objects.all().order_by('-pk')
    context = {'changelogs': changelogs}

    return render(request, 'mainpages/changelogs.html', context)
