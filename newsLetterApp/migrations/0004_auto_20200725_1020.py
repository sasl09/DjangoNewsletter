# Generated by Django 3.0.8 on 2020-07-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetterApp', '0003_newsletteruser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
