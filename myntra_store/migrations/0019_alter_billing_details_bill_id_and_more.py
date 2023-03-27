# Generated by Django 4.1.7 on 2023-03-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0018_alter_billing_details_bill_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='shipp_city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='shipp_country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='27-03-2023 15:02:11', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='customercontactus',
            name='customer_contact_us_id',
            field=models.CharField(default='CON27M0211948', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, default='27-03-2023 15:02:11', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR27M0211937', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribe_to_newsletter',
            name='subscribtion_id',
            field=models.CharField(default='SUB27M0211948', max_length=100),
        ),
    ]
