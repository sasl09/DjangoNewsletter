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
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from users import views as user_views
from django.views.generic import TemplateView
from emailer import views
from newsLetterApp import views as newsletterapp_views
from newsLetterApp.views import NewslettersViewSet, UsersViewSet, TagsViewSet, SubscribersViewSet
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view


API_TITLE = 'Newsletter API'
API_DESCRIPTION = 'Api de un newsletter.'
schema_view = get_swagger_view(title=API_TITLE)

=======
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
>>>>>>> b45c2250c6ca585848e16ee36ed4d5b47c91bea1
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd

router = routers.DefaultRouter()
router.register(r'newsletters', NewslettersViewSet, "Newsletters")
router.register(r'tags', TagsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'subscribers', SubscribersViewSet)


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^newsLetter/', include('newsLetterApp.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('update_profile/', user_views.update_profile, name='update_profile'),
    path('profile/', user_views.profile, name='profile'),
    path('profiles/', user_views.profiles, name='profiles'),
    # path('author_profile/', user_views.author_profile, name='author_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('newsLetterApp.urls')),
    path('newsletter_subscribe/', newsletterapp_views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter_unsubscribe/', newsletterapp_views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
    path('confirm_email/', newsletterapp_views.confirm_email, name='confirm_email'),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send_email/', views.SendFormEmail.as_view(), name='send_email'),
    # API URLS:
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
<<<<<<< HEAD
    # SWAGGER URL:
    path('docs/', schema_view),

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
]

# This code's for our media:

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
]
>>>>>>> b45c2250c6ca585848e16ee36ed4d5b47c91bea1
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
