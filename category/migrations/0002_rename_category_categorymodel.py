# Generated by Django 5.0.6 on 2024-06-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryModel',
        ),
    ]
