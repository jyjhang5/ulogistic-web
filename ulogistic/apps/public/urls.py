from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('index', views.index),
	path('newslist', views.newslist),
	path('news/<int:id>/', views.news),
	path('hr', views.hr),
]