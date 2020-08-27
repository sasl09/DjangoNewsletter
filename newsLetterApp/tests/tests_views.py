from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from newsLetterApp.models import Tag, TagsNewsletter, Subscriber
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')
        self.newsletter_main_url = reverse('newsletter_main')
        self.newsletter_bulletins_url = reverse('newsletter_bulletins')
        self.newsletter_categories_url = reverse('newsletter_categories')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    # Here you can add a "POST" test for our "register" view...
    def test_register_POST(self):
        response = self.client.post(self.register_url, data={
            'username': 'testUsr',
            'email': 'testUsr@gmail.com',
            'password1': 'Iluminati09',
            'password1': 'Iluminati09',
            'account_type': True
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    # Disable the "login@required" decorator before running this test, otherwise it will throw an HTTP.response 302.
    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_newsletter_main_GET(self):
        response = self.client.get(self.newsletter_main_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsLetterApp/main.html')

    def test_newsletter_bulletins_GET(self):
        response = self.client.get(self.newsletter_bulletins_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsLetterApp/bulletins.html')

    def test_newsletter_categories_GET(self):
        response = self.client.get(self.newsletter_categories_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsLetterApp/categories.html')

