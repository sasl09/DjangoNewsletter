# Generated by Django 3.0.8 on 2020-07-28 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsLetterApp', '0004_auto_20200725_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='newsletteruser',
            name='users',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('newsletters_included', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsLetterApp.Newsletter')),
            ],
        ),
    ]
