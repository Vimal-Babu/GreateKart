# Generated by Django 4.2.4 on 2023-09-28 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_net_amount_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='net_amount',
        ),
        migrations.DeleteModel(
            name='Net_amount',
        ),
    ]
