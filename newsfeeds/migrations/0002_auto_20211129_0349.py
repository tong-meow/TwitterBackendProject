# Generated by Django 3.1.3 on 2021-11-29 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsfeed',
            options={'ordering': ('user', '-created_at')},
        ),
    ]
