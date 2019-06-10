from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls import reverse
from django.views import generic

# from .models import Choice, Question

# from .models import Choice, Question

app_name = 'world'


# class IndexView(generic.ListView):
#     template_name = 'index.html'
def index(request):
    return HttpResponse("Hello, world. You're at the world index.")
