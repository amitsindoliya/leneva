# Generated by Django 3.1 on 2020-08-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leneva_backend', '0007_auto_20200809_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]