from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('sign_in', views.sign_in, name='fun time'),
    path('create', views.create, name='create'),
]
