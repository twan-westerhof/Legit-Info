# Generated by Django 3.0.8 on 2020-08-03 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0002_impact'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='hierarchy',
            field=models.CharField(default='world', max_length=255),
            preserve_default=False,
        ),
    ]