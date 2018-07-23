from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('tt', views.test, name='tt'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),


]