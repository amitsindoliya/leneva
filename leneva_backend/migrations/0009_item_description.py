# Generated by Django 3.1 on 2020-08-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leneva_backend', '0008_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
