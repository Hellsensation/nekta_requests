# Generated by Django 4.2.7 on 2023-11-06 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SomeRequests', '0003_rename_request_userrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SomeRequests.userrequest')),
            ],
        ),
    ]
