# Generated by Django 4.2.4 on 2023-09-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orders_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=0),
            preserve_default=False,
        ),
    ]