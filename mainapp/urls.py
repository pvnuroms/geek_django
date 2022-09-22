from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

from mainapp import views

# urlpatterns = [
#     # path('', views.check_kwargs),
#     path('', views.HelloWorldView.as_view()),
#     path('<str:word>/', views.check_kwargs),
# ]
#
# urlpatterns = [
#     path('', views.HelloWorldView.as_view()),
#     path('<str:word>/', views.check_kwargs),
# ]