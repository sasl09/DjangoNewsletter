# Generated by Django 3.0.8 on 2020-08-04 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetterApp', '0030_tagsnewsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='author',
        ),
    ]