# Generated by Django 3.0.8 on 2020-08-05 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200804_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='prof_location',
            new_name='location',
        ),
    ]