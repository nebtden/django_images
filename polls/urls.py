from django.urls import path

from . import views

urlpatterns = [
    path('tt', views.test, name='tt'),
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detail, name='testid'),


]