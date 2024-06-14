from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^contact/', views.contact, name='contact'),
]