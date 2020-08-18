# Generated by Django 3.0.8 on 2020-08-04 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsLetterApp', '0022_auto_20200803_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='bulletins',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newsLetterApp.Tag'),
        ),
    ]