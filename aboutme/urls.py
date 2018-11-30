from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('login/', LoginView.as_view(template_name= 'aboutme/login.html'),name="login"),
    path('register/',views.register, name='register')]
