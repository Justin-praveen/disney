# Generated by Django 5.0.7 on 2024-07-15 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_arrival',
            name='key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]