# Generated by Django 5.0.2 on 2024-02-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Videos', '0004_remove_likes_like_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_code',
            field=models.CharField(default=1979, max_length=264),
            preserve_default=False,
        ),
    ]