# Generated by Django 3.0.8 on 2020-08-04 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsLetterApp', '0024_auto_20200803_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='TagsNewsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsLetterApp.Newsletter')),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsLetterApp.Tag')),
            ],
        ),
    ]