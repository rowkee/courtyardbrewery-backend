# Generated by Django 4.2.7 on 2023-11-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_user_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='merch',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
