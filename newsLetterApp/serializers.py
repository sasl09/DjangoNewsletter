from rest_framework import serializers
from .models import TagsNewsletter, Tag, Subscriber
<<<<<<< HEAD
from users.models import Profile
=======
<<<<<<< HEAD
from users.models import Profile
=======
<<<<<<< HEAD
from users.models import Profile
=======
<<<<<<< HEAD
from users.models import Profile
=======
>>>>>>> b45c2250c6ca585848e16ee36ed4d5b47c91bea1
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
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


