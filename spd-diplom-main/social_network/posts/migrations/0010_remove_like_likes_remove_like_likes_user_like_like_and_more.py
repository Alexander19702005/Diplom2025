# Generated by Django 5.0.2 on 2025-02-12 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_message_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='like',
            name='likes_user',
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
