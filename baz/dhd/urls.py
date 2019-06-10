from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import storage
from . import views

app_name = 'dhd'

urlpatterns = [
    # Home
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('dhd/', views.dhd, name="dhd"),
    path('menu/', views.menu, name="menu"),
    path('logindhd/', views.logindhd, name="logindhd"),
    path('testpage/', views.testpage, name="testpage"),
    path('lts/', views.lts, name="lts"),

    # # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    #
    # # ex: /polls/5/
    # path('testpage/', views.TestpageView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # path('blog/', views.BlogView.as_view(), name='blog'),
    # # ex: /polls/5/vote/
    # path('dhd/', views.DhdView.as_view(), name='dhd'),

]
