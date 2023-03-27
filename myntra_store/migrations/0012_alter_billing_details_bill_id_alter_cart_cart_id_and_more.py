# Generated by Django 4.1.7 on 2023-03-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0011_order_provider_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='27-03-2023 12:32:06', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_city',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_country',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_pincode',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_state',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_email',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_phone',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='customercontactus',
            name='customer_contact_us_id',
            field=models.CharField(default='CON27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR27M3206640', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribe_to_newsletter',
            name='subscribtion_id',
            field=models.CharField(default='SUB27M3206640', max_length=100),
        ),
    ]
