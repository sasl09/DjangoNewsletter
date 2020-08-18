# Generated by Django 2.2.14 on 2020-08-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('newsLetterApp', '0038_usergroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='group',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
