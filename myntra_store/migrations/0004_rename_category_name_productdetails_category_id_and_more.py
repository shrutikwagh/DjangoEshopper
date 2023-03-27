# Generated by Django 4.1.7 on 2023-03-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0003_alter_billing_details_bill_id_alter_cart_cart_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetails',
            old_name='category_name',
            new_name='category_id',
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI12M0253039', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR12M0253039', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='12-03-2023 21:02:53', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC12M0253031', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS12M0253031', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD12M0253039', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR12M0253031', max_length=100),
        ),
    ]
