from django.db import models
from datetime import date, datetime
import time
import string, random

# Create your models here.

def GenSequenceId(val):
    profileId = val[0:3]
    currentMinutes = datetime.now().strftime("%M")
    currentSeconds = datetime.now().strftime("%S")
    year = time.strftime("%y", time.localtime())
    month = time.strftime("%m", time.localtime())
    day = time.strftime("%d", time.localtime())
    s = '{:03.0f}'.format(datetime.now().microsecond / 1000.0)
    profileId = profileId + str(day) + 'M' + str(currentMinutes) + str(currentSeconds) + str(s)
    # print(profileId)
    return profileId



class Category(models.Model):
    category_id=models.CharField(max_length=100,default=GenSequenceId("CC"))
    category_name = models.CharField(max_length = 200)
    description = models.TextField()

    class Meta:
        db_table = "Category"

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        # return '{}{}{}'.format(self.category_id,"-", self.category_name)
        return '{}'.format(self.category_name)

class ProductDetails(models.Model):
    product_id=models.CharField(max_length=100,default=GenSequenceId("PR"))
    product_name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    # category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/')

    # @staticmethod
    # def get_all_Products_per_Categories(category_name1):
    #     filter_products=ProductDetails.objects.filter(category_id=category_name1)
    #     return filter_products


class Customer(models.Model):
    customer_id=models.CharField(max_length=100,default=GenSequenceId("CUS"))
    first_name = models.CharField(max_length=50,default=None)
    last_name = models.CharField(max_length=50,default=None)
    phone = models.CharField(max_length=15,default=None)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    created_at = models.CharField(max_length=500,default=None)
    bill_address_line1=models.TextField(null=True, blank=True)
    bill_address_line2=models.TextField(null=True, blank=True)
    bill_country = models.CharField(max_length=500,null=True, blank=True)
    bill_city = models.CharField(max_length=500 ,null=True, blank=True)
    bill_state = models.CharField(max_length=500 ,null=True, blank=True)
    bill_pincode = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_phone = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_email = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_address_line1=models.TextField(null=True, blank=True)
    shipp_address_line2=models.TextField(null=True, blank=True)
    shipp_country = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_city = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_state = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_pincode = models.CharField(max_length=500 ,null=True, blank=True)






    @staticmethod
    def get_customer_by_phone(phone):

        return Customer.objects.get(phone=phone)

    @staticmethod
    def get_customer_by_cust_id(cust_id):
        return Customer.objects.get(customer_id=cust_id)


    # def __str__(self):
    #
    #     return self.phone


class Order(models.Model):
    order_id = models.CharField(max_length=100, default=GenSequenceId("OD"))
    product_id = models.CharField(max_length=50, blank=True)
    customer_id = models.CharField(max_length=50, blank=True)
    provider_order_id = models.CharField(max_length=50, blank=True)
    sub_total_price=models.CharField(max_length=50, blank=True,null=True)
    shipping_charges=models.CharField(max_length=50, blank=True,null=True)
    total_price=models.CharField(max_length=50, blank=True,null=True)
    quantity = models.CharField(max_length=50, blank=True,null=True)
    product_price = models.CharField(max_length=50, blank=True,null=True)
    cart_id = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, default=datetime.now().strftime("%d-%m-%Y %H:%M:%S"), blank=True)


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, default=GenSequenceId("CAR"))
    customer_id = models.CharField(max_length=50, default='', blank=True)
    product_id= models.CharField(max_length=50, default='', blank=True)
    total_price= models.CharField(max_length=50, default='', blank=True)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    user_name = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.CharField(max_length=50, default=datetime.now().strftime("%d-%m-%Y %H:%M:%S"), blank=True)

    class Meta:
        db_table = "Cart"


class Billing_Details(models.Model):
    bill_id=models.CharField(max_length=100,default=GenSequenceId("BI"))
    customer_id=models.CharField(max_length=50,null=True, blank=True)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    email = models.CharField(max_length=55,null=True, blank=True)
    password = models.CharField(max_length=500,null=True, blank=True)
    created_at = models.CharField(max_length=500 ,null=True, blank=True)
    bill_address_line1=models.TextField(null=True, blank=True)
    bill_address_line2=models.TextField(null=True, blank=True)
    bill_country = models.CharField(max_length=500,null=True, blank=True)
    bill_city = models.CharField(max_length=500,null=True, blank=True)
    bill_state = models.CharField(max_length=500,null=True, blank=True)
    bill_pincode = models.CharField(max_length=500,null=True, blank=True)
    shipp_phone = models.CharField(max_length=500,null=True, blank=True)
    shipp_email = models.CharField(max_length=500,null=True, blank=True)
    shipp_address_line1=models.TextField(null=True, blank=True)
    shipp_address_line2=models.TextField(null=True, blank=True)
    shipp_country = models.CharField(max_length=500,null=True, blank=True)
    shipp_city = models.CharField(max_length=500,null=True, blank=True)
    shipp_state = models.CharField(max_length=500 ,null=True, blank=True)
    shipp_pincode = models.CharField(max_length=500 ,null=True, blank=True)
    product_id=models.CharField(max_length=500 ,null=True, blank=True)
    product_name= models.CharField(max_length=150, default='', blank=True)
    order_id=models.CharField(max_length=150, default='', blank=True)

    product_price=models.CharField(max_length=500 ,null=True, blank=True)
    product_quantity=models.CharField(max_length=500 ,null=True, blank=True)
    sub_total_price=models.CharField(max_length=500 ,null=True, blank=True)
    shipping_charges=models.CharField(max_length=500 ,null=True, blank=True)
    total_price=models.CharField(max_length=500 ,null=True, blank=True)
    cart_id=models.CharField(max_length=500 ,null=True, blank=True)


class CustomerContactUs(models.Model):
    customer_contact_us_id=models.CharField(max_length=100,default=GenSequenceId("CON"))
    name = models.CharField(max_length=100)
    customer_id=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    created_at = models.CharField(max_length=500 ,null=True, blank=True)

    class Meta:
        db_table = "CustomerContactUs"



class Subscribe_to_NewsLetter(models.Model):
    subscribtion_id=models.CharField(max_length=100,default=GenSequenceId("SUB"))
    name = models.CharField(max_length=100)
    customer_id=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    created_at = models.CharField(max_length=500 ,null=True, blank=True)

    class Meta:
        db_table = "Subscribe_to_NewsLetter"


