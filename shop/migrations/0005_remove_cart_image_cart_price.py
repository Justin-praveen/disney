# Generated by Django 4.2.11 on 2024-07-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
