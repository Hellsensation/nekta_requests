# Generated by Django 4.2.7 on 2023-11-06 07:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SomeRequests', '0002_request_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='UserRequest',
        ),
    ]
