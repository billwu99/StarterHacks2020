from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    # ex: /user/
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    #path('personaldata/', views.PersonalData.as_view(), name='personaldata'),
    url(r'^data$', views.data, name='data'),
    path('search/<str:input>/', views.search_box, name='search')

]