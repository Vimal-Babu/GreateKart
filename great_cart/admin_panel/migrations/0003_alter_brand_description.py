# Generated by Django 4.2.4 on 2023-08-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_remove_category_category_image_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]