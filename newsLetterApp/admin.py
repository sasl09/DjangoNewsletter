from django.contrib import admin
from .models import Tag, TagsNewsletter, Subscriber

admin.site.register(Tag)
admin.site.register(TagsNewsletter)
admin.site.register(Subscriber)

