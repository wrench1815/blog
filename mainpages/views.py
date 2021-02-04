from django.shortcuts import render


def home(request):
    return render(request, 'mainpages/home.html')


def about(request):
    return render(request, 'mainpages/about.html')


def contactMe(request):
    return render(request, 'mainpages/contact_me.html')
