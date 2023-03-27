# Generated by Django 4.1.7 on 2023-03-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myntra_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetails',
            old_name='category_id',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='bill_id',
            field=models.CharField(default='BI12M2555578', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='CAR12M2555578', max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.CharField(blank=True, default='12-03-2023 20:25:55', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='CC12M2555578', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_country',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_pincode',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bill_state',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CUS12M2555578', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_country',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_phone',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_pincode',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shipp_state',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='OD12M2555578', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.CharField(default='PR12M2555578', max_length=100),
        ),
    ]
