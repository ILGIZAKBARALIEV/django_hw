# Generated by Django 5.1.5 on 2025-02-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myordersmodel',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='укажите адрес доставки'),
        ),
    ]
