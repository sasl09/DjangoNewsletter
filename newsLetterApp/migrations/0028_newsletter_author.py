# Generated by Django 3.0.8 on 2020-08-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetterApp', '0027_remove_newsletter_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
