# Generated by Django 5.1.6 on 2025-02-21 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Library_kg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('address', models.TextField(blank=True, null=True, verbose_name='укажите адрес доставки')),
                ('choice_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library_kg.bookmodel', verbose_name='Книга')),
            ],
        ),
    ]
