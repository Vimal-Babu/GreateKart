# Generated by Django 4.2.4 on 2023-09-06 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]