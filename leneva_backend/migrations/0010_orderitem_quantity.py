# Generated by Django 3.1 on 2020-08-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leneva_backend', '0009_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
