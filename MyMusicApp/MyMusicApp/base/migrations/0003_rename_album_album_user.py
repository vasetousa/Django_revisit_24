# Generated by Django 5.0.3 on 2024-03-20 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_album_album_alter_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album',
            new_name='user',
        ),
    ]