# Generated by Django 3.1 on 2020-08-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leneva_backend', '0003_auto_20200809_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('V', 'Vegtables'), ('F', 'Fruit'), ('O', 'Others')], default='V', max_length=2),
        ),
    ]
