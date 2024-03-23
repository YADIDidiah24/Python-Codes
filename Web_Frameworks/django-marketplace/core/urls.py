from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
app_name='core'
from .forms import LoginForm
urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.signup, name='signup'),
    
]