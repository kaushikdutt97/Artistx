# Generated by Django 4.1.3 on 2022-11-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_alter_artistsprofile_on_break'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistsprofile',
            name='on_break',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
