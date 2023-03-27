from django.contrib import admin
# Register your models here.
from .models import Category,ProductDetails,Customer,Order,CustomerContactUs,Subscribe_to_NewsLetter,Billing_Details

class AdminProductDetails(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

class AdminCustomerContactUs(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

class AdminSubscribe_to_NewsLetter(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

class AdminBilling_Details(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']


admin.site.register(Category)
admin.site.register(ProductDetails)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CustomerContactUs)
admin.site.register(Subscribe_to_NewsLetter)
admin.site.register(Billing_Details)
