# Generated by Django 5.1.1 on 2024-11-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='episode',
            name='season_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='episode_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='season_number',
            field=models.PositiveIntegerField(),
        ),
    ]
