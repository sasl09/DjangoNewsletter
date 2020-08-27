# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from newsLetterApp.views import newsletter_main, newsletter_subscribe, \
#     newsletter_bulletins, newsletter_categories, newsletter_unsubscribe, confirm_email
# from users.views import register, profile
#
#
# class TestsUrls(SimpleTestCase):
#
#     def test_register_url_is_resolved(self):
#         url = reverse('register')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, register)
#
#     def test_profile_url_is_resolved(self):
#         url = reverse('profile')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, profile)
#
#     def test_login_url_is_resolved(self):
#         url = reverse('login')
#         print(resolve(url))
#
#     def test_logout_url_is_resolved(self):
#         url = reverse('logout')
#         print(resolve(url))
#
#     def test_newsletter_main_url_is_resolved(self):
#         url = reverse('newsletter_main')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, newsletter_main)
#
#     def test_newsletter_bulletins_url_is_resolved(self):
#         url = reverse('newsletter_bulletins')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, newsletter_bulletins)
#
#     def test_newsletter_categories_url_is_resolved(self):
#         url = reverse('newsletter_categories')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, newsletter_categories)
#
#     def test_newsletter_subscribe_url_is_resolved(self):
#         url = reverse('newsletter_subscribe')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, newsletter_subscribe)
#
#     def test_newsletter_unsubscribe_url_is_resolved(self):
#         url = reverse('newsletter_unsubscribe')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, newsletter_unsubscribe)
#
#     def test_confirm_email_url_is_resolved(self):
#         url = reverse('confirm_email')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, confirm_email)
#
#     def test_home_url_is_resolved(self):
#         url = reverse('home')
#         print(resolve(url))
#
#     def test_send_email_url_is_resolved(self):
#         url = reverse('send_email')
#         print(resolve(url))
#
#
#     # TEST API ROUTER URLS HERE:
#
#
