<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from newsLetterApp.views import newsletter_main, newsletter_subscribe, \
    newsletter_bulletins, newsletter_categories, newsletter_unsubscribe, confirm_email
from users.views import register, profile


class TestsUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))

    def test_newsletter_main_url_is_resolved(self):
        url = reverse('newsletter_main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newsletter_main)

    def test_newsletter_bulletins_url_is_resolved(self):
        url = reverse('newsletter_bulletins')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newsletter_bulletins)

    def test_newsletter_categories_url_is_resolved(self):
        url = reverse('newsletter_categories')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newsletter_categories)

    def test_newsletter_subscribe_url_is_resolved(self):
        url = reverse('newsletter_subscribe')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newsletter_subscribe)

    def test_newsletter_unsubscribe_url_is_resolved(self):
        url = reverse('newsletter_unsubscribe')
        print(resolve(url))
        self.assertEquals(resolve(url).func, newsletter_unsubscribe)

    def test_confirm_email_url_is_resolved(self):
        url = reverse('confirm_email')
        print(resolve(url))
        self.assertEquals(resolve(url).func, confirm_email)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))

    def test_send_email_url_is_resolved(self):
        url = reverse('send_email')
        print(resolve(url))


    # TEST API ROUTER URLS HERE:


>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2
>>>>>>> 28a4ca38c4cd9385736f9ad15eeb5ae7488ffd53
