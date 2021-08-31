from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import ChangelogsModel, ContactForm


def home(request):
    return render(request, 'mainpages/home.html')


def about(request):
    site_owner = User.objects.filter(username__exact='wrench1815').first()

    context = {'site_owner': site_owner}
    return render(request, 'mainpages/about.html', context)


def contactMe(request):
    return render(request, 'mainpages/contact_me.html')


def changelogs(request):
    changelogs = ChangelogsModel.objects.all().order_by('-pk')
    context = {'changelogs': changelogs}

    return render(request, 'mainpages/changelogs.html', context)


class ContactForm(SuccessMessageMixin, CreateView):
    model = ContactForm
    fields = ['full_name', 'email', 'message']
    success_message = 'Thank you <span class="text-primary text-gradient fw-bold">%(full_name)s</span> for reaching out.'

    def get_success_url(self):
        return reverse('contactMe')
