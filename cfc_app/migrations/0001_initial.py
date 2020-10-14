# Generated by Django 3.0.8 on 2020-10-10 13:06

import cfc_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=80, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=80)),
                ('shortname', models.CharField(max_length=20)),
                ('hierarchy', models.CharField(max_length=200)),
                ('govlevel', models.CharField(max_length=80)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='cfc_app.Location')),
            ],
            options={
                'ordering': ['hierarchy'],
            },
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=cfc_app.models.get_default_law_key, max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=1000)),
                ('impact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laws', to='cfc_app.Impact')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laws', to='cfc_app.Location')),
            ],
            options={
                'verbose_name_plural': 'laws',
            },
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('impacts', models.ManyToManyField(to='cfc_app.Impact')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='criteria', to='cfc_app.Location')),
            ],
            options={
                'verbose_name_plural': 'criteria',
            },
        ),
    ]