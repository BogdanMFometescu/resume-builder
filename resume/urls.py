from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('resumes/', views.resumes, name='resumes'),
               path('resume/<str:pk>/', views.resume, name='resume'),
               path('create-resume', views.create_resume, name='create-resume'),
               path('update-resume/<str:pk>/', views.update_resume, name='update'),
               path('delete-resume/<str:pk>/', views.delete_resume, name='delete'),
               path('add-experience', views.add_experience, name='experience'),
               path('update-experience/<str:pk>/', views.update_experience, name='update-experience'),
               path('add-new-experience/<uuid:pk>/', views.add_new_experience, name='add-new-experience'),
               path('delete-experience/<str:pk>/', views.delete_experience, name='delete-experience'),
               path('add-education', views.add_education, name='education'),
               path('update-education/<str:pk>/', views.update_education, name='update-education'),
               path('delete-education/<str:pk>/', views.delete_education, name='delete-education'),
               path('add-project', views.add_project, name='project'),
               path('update-project/<str:pk>/', views.update_project, name='update-project'),
               path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),
               path('add-skill', views.add_skill, name='skill'),
               path('update-skill/<str:pk>/', views.update_skill, name='update-skill'),
               path('delete-skill/<str:pk>/', views.delete_skill, name='delete-skill'),
               path('make-pdf/<str:pk>/', views.make_pdf, name='make_pdf'),
               path('export-to-pdf', views.export_to_pdf, name='export-to-pdf')
               ]
