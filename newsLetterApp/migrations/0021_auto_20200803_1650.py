# Generated by Django 3.0.8 on 2020-08-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetterApp', '0020_auto_20200803_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='bulletins',
            field=models.ManyToManyField(to='newsLetterApp.Newsletter'),
        ),
    ]