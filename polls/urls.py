from django.urls import path

from . import views

urlpatterns = [
    path('tt', views.test, name='test'),
    path('', views.index, name='index'),

]