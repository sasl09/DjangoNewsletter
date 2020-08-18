from django.conf.urls import url
from django.urls import path
from .views import newsletter_main, newsletter_bulletins, newsletter_sports


urlpatterns = [
    url(r'main/$', newsletter_main, name='newsletter_main'),
    url(r'bulletins/$', newsletter_bulletins, name='newsletter_bulletins'),
    url(r'sports/', newsletter_sports, name='newsletter_sports'),
]


