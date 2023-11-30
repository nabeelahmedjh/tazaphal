from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registrationView, name='register'),
    path('contact/', views.contact, name='contact')
]
