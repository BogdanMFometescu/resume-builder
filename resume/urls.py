from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
               path('resumes/', views.resumes, name='resumes'),
               path('resume/<str:pk>/', views.resume, name='resume'),
               path('create-resume', views.create_resume, name='create-resume'),
               path('update-resume/<str:pk>/', views.update_resume, name='update'),
               path('delete-resume/<str:pk>/', views.delete_resume, name='delete'),
               path('add-experience', views.add_experience, name='experience'),
               path('add-education', views.add_education, name='education'),
               path('add-project', views.add_project, name='project'),
               path('add-skill', views.add_skill, name='skill'),
               path('make-pdf/<str:pk>/',views.make_pdf, name='make_pdf'),
               path('export-to-pdf',views.export_to_pdf,name='export-to-pdf')
               ]
