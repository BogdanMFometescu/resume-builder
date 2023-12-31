from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('resumes/', views.resumes, name='resumes'),
               path('resume/<uuid:pk>/', views.resume, name='resume'),
               path('create-resume/', views.create_resume, name='create-resume'),
               path('update-resume/<uuid:pk>/', views.update_resume, name='update'),
               path('delete-resume/<uuid:pk>/', views.delete_resume, name='delete'),
               path('add-experience/', views.create_experience, name='experience'),
               path('update-experience/<uuid:pk>/', views.update_experience, name='update-experience'),
               path('add-new-experience/<uuid:pk>/', views.add_new_experience, name='add-new-experience'),
               path('delete-experience/<uuid:pk>/', views.delete_experience, name='delete-experience'),
               path('add-education/', views.create_education, name='education'),
               path('add-new-education/<uuid:pk>/', views.add_new_education, name='add-new-education'),
               path('update-education/<uuid:pk>/', views.update_education, name='update-education'),
               path('delete-education/<uuid:pk>/', views.delete_education, name='delete-education'),
               path('add-project/', views.create_project, name='project'),
               path('add-new-project/<uuid:pk>', views.add_new_project, name='add-new-project'),
               path('update-project/<uuid:pk>/', views.update_project, name='update-project'),
               path('delete-project/<uuid:pk>/', views.delete_project, name='delete-project'),
               path('add-skill/', views.create_skill, name='skill'),
               path('add-new-skill/<uuid:pk>/', views.add_new_skill, name='add-new-skill'),
               path('update-skill/<uuid:pk>/', views.update_skill, name='update-skill'),
               path('delete-skill/<uuid:pk>/', views.delete_skill, name='delete-skill'),
               path('make-pdf/<uuid:pk>/', views.make_pdf, name='make_pdf'),
               path('export-to-pdf/', views.export_to_pdf, name='export-to-pdf')
               ]
