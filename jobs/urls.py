from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs, name='job-listings'),
    path('details/<slug:job_slug>/', views.details, name='details'),
    path('details/<slug:job_slug>/register/', views.register, name='register'),
    path('details/<slug:job_slug>/register/success/', views.success, name='success'),
] 