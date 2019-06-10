from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'world'

urlpatterns = [
    path('', views.index, name='index'),
    # # Home
    # path('admin/', admin.site.urls),
    # # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    # # ex: /polls/5/
    # path('testpage/', views.TestpageView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # path('blog/', views.BlogView.as_view(), name='blog'),
    # # ex: /polls/5/vote/
    # path('dhd/', views.DhdView.as_view(), name='dhd'),

]
