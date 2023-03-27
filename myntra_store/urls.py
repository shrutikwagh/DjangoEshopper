from django.contrib import admin
from django.urls import path
from . import views as v
# from .views.signup import Signup
# from .views.login import Login , logout
# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .middlewares.auth import  auth_middleware

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',v.index , name='homepage'),
    path('dress_category/<categoryID>', v.dress_category , name='dress_category'),

    path('signup/', v.Signup_page, name='signup'),
    path('login_page/', v.login_page, name='login_page'),
    path('delete_view/', v.delete_view, name='delete_view'),
    path('logout/', v.logout , name='logout'),
    path('UpdateItem/', v.UpdateItem , name='UpdateItem'),
    path('Sendmail/', v.Sendmail , name='Sendmail'),
    path('checkout/', v.checkout , name='checkout'),
    path('add_to_cart/', v.add_to_cart, name='add_to_cart'),
    path('Contact_Us/', v.Contact_Us, name='AboutUs'),
    path('About_Us/', v.About_Us, name='AboutUs'),
    path('Payment_pagw/', v.Payment_pagw, name='Payment_pagw'),
    path('intiate_payment/', v.intiate_payment, name='intiate_payment'),
    path('paymenthandler/', v.paymenthandler, name='paymenthandler'),
    path('delete_view1/', v.delete_view1, name='delete_view1'),

    path('submit_subscription_of_newsletter/', v.submit_subscription_of_newsletter, name='submit_subscription_of_newsletter'),
    path('view_bill/<order_id>/', v.view_bill,name="view_bill"),

]
if settings.DEBUG:
        print(static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT),'&&&&&&&&&&&&&&&&&&&')
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
