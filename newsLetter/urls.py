"""newsLetter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.views.generic import TemplateView
from emailer import views
from newsLetterApp import views as newsletterapp_views
from newsLetterApp.views import newsletters_list


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^newsLetter/', include('newsLetterApp.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('newsLetterApp.urls')),
    path('newsletter_subscribe/', newsletterapp_views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter_unsubscribe/', newsletterapp_views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
    path('confirm_email/', newsletterapp_views.confirm_email, name='confirm_email'),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send_email/', views.SendFormEmail.as_view(), name='send_email'),
    # API URLS:
    url(r'^api/v1/', newsletters_list),
]