# Generated by Django 4.2.4 on 2023-10-06 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_searchquery_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchquery',
            name='product',
        ),
    ]
