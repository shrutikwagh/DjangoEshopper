# Generated by Django 4.1.7 on 2023-03-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0002_rename_category_id_productdetails_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI12M5745995', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR12M5745995', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='12-03-2023 20:57:45', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC12M5745979', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS12M5745979', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD12M5745995', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR12M5745979', max_length=100),
        ),
    ]
