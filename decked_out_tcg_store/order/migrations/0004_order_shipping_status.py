# Generated by Django 4.2.9 on 2024-01-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_first_name_order_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('in_process', 'In Process'), ('shipped', 'Shipped')], default='ordered', max_length=20),
        ),
    ]
