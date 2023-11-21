from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('resumes/', views.resumes, name='resumes'),
               path('resume/<str:pk>/', views.resume, name='resume'),
               path('create-resume', views.create_resume, name='create-resume'),
               path('update-resume/<str:pk>/', views.update_resume, name='update'),
               path('delete-resume/<str:pk>/', views.delete_resume, name='delete'),
               ]
