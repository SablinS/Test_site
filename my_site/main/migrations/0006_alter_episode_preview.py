# Generated by Django 5.1.1 on 2024-10-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_episode_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='preview',
            field=models.ImageField(blank=True, default=None, upload_to='previews/'),
            preserve_default=False,
        ),
    ]