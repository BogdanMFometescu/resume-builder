from django.urls import path
from . import views

urlpatterns = [path('login/', views.login_user, name='login'),
               path('logout/', views.logout_user, name='logout'),
               path('account/', views.user_account, name='account'),
               path('edit-account/', views.edit_account, name='edit-account'),
               path('register-user/', views.register_user, name='register'),
               path('profiles/', views.profiles, name='profiles'),
               path('profile/<uuid:pk>/', views.user_profile, name='user-profile')]