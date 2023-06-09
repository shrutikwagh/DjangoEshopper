# Generated by Django 4.1.7 on 2023-03-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0016_rename_address_order_cart_id_remove_order_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_charges',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='27-03-2023 14:50:03', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='customercontactus',
            name='customer_contact_us_id',
            field=models.CharField(default='CON27M5003543', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, default='27-03-2023 14:50:03', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR27M5003535', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribe_to_newsletter',
            name='subscribtion_id',
            field=models.CharField(default='SUB27M5003543', max_length=100),
        ),
    ]
