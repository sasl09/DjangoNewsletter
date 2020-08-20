from rest_framework import serializers
from .models import TagsNewsletter, Tag, Subscriber
from django.contrib.auth.models import User


class NewsletterSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField(max_length=100)

    class Meta:
        model = TagsNewsletter
        fields = ('id', 'tags', 'title', 'date_added', 'content', 'author')


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'description')


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class SubscribersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email', 'confirmed')


