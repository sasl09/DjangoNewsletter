from rest_framework import serializers
from .models import TagsNewsletter


class NewsletterSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=100)

    class Meta:
        model = TagsNewsletter
        fields = ('id', 'tags', 'title', 'date_added', 'content', 'author')




