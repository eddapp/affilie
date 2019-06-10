from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.conf.urls import include, url
from django.contrib import admin
from django.views import generic, static
from django.urls import include, path

app_name = 'dhd'


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def dhd(request):
    return render(request, 'dhd.html')


def logindhd(request):
    return render(request, 'logindhd.html')


def menu(request):
    return render(request, 'menu.html')


def testpage(request):
    return render(request, 'testpage.html')


def lts(request):
    return render(request, 'lts.html')

# # Create your views here.
#
# class BlogView(generic.ListView):
#     template_name = 'blog.html'
#
#
# class DhdView(generic.ListView):
#     template_name = 'dhd.html'
#
#
# class IndexView(generic.ListView):
#     template_name = 'index.html'
#
#
# class LogindhdView(generic.ListView):
#     template_name = 'logindhd.html'
#
#
# class LtsView(generic.ListView):
#     template_name = 'lts.html'
#
#
# class MenuView(generic.ListView):
#     template_name = 'menu.html'
#
#
# class TestpageView(generic.ListView):
#     template_name = 'testpage.html'
