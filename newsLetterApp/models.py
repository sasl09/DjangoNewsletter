from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class TagsNewsletter(models.Model):
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


