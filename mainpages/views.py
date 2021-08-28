from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from .models import ChangelogsModel, ContactForm


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


class ContactForm(SuccessMessageMixin, CreateView):
    model = ContactForm
    fields = ['full_name', 'email', 'message']
    success_message = 'Thank you <span class="text-primary text-gradient fw-bold">%(full_name)s</span> for reaching out.'

    def get_success_url(self):
        return reverse('contactMe')


# def contactform(request):
#     if request.method == 'POST':
#         full_name = request.POST['full_name']
#         email = request.POST['email']
#         message = request.POST['message']

#         contact_form = ContactForm(full_name=full_name,
#                                    email=email,
#                                    message=message)
#         contact_form.save()

#     return redirect('contactMe')
