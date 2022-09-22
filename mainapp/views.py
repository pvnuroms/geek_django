# from django.shortcuts import render
# from django.views.generic import View

from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# def hello_world(request):
#     return HttpResponse('Hello')
#
#
# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwargs:\n{kwargs}')
#
#
# class HelloWorldView(View):
#     def get(self, *args):
#         return HttpResponse('Hello again')


class MainPAgeView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/doc_site.html'