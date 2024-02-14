# Generated by Django 5.0.2 on 2024-02-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Videos', '0006_alter_video_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-updated_at', '-created_at', 'title']},
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
