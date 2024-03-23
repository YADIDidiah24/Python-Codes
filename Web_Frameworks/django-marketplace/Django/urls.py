from django.contrib import admin
from django.urls import path, include
from core.views import index,contact,signup
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.forms import LoginForm
urlpatterns = [
    path('',index, name="index"),
    path('contact/', contact, name="contact"),
    path('items/',include('item.urls')),
    path('admin/', admin.site.urls),
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
