# Generated by Django 4.1.3 on 2022-11-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistsprofile',
            old_name='users',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='users',
            new_name='profile',
        ),
    ]