import json
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from datetime import date, datetime
import time
import string, random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay
from .constants import PaymentStatus
from .models import Category,Customer,ProductDetails,Cart,Order,Billing_Details,CustomerContactUs,Subscribe_to_NewsLetter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
import requests
from django.db.models import Count
from django.core.mail import send_mail
# from .mail_send import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))





def index(request):

    user_name=''
    try:
        user_name=request.session['user_name']
        customer_id=request.session['customer_id']

    except KeyError:
        request.session['user_name'] = ''
        customer_id=''


    categories = Category.objects.all()

    Cart_query = Cart.objects.filter(customer_id=customer_id)

    print(categories,'categories categories')

    productdetails2 = ProductDetails.objects.all()
    productdetails1 = ProductDetails.objects.values('category_id').annotate(dcount=Count('category_id')).order_by('category_id')
    cart_quanty=[]
    count_of_cart=0
    for i in Cart_query:
        cart_quanty.append(i.quantity)
        product_items = ProductDetails.objects.get(product_id=i.product_id)
        i.product_name=product_items.product_name

    for num  in cart_quanty:
        count_of_cart += num
        print(count_of_cart,'yiuuyuy')


    for i in productdetails1:

        category_name = Category.objects.get(id=i['category_id'])

        i['category_name']=category_name
    print(productdetails1, "productdetails1")

    context = {'categories': categories,'user_name': user_name,'count_of_cart':count_of_cart,'productdetails1':productdetails1,'productdetails2':productdetails2}


    return render(request, 'index.html',context)



def Signup_page(request):

    try:
        user_name=request.session['user_name']
        customer_id=request.session['customer_id']

    except KeyError:
        request.session['user_name'] = ''
        customer_id=''


    try:

        print('Received Post Request',request.POST)
        postData=request.POST
        first_name=postData.get("firstname")
        last_name=postData.get("lastname")
        phone=postData.get("phone")
        email=postData.get("email")
        password=postData.get("password")
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        customer_id=GenSequenceId("CUS")

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password,
                            created_at=created_at, customer_id=customer_id)

        customer.save()
        print()
        request.session['customer_mobile'] = phone
        request.session['customer_id'] = customer_id
        request.session['user_name'] = first_name + " " + last_name
        print(request.session['customer_id'])

        return redirect(index)
    except Exception as e:
        print(e,'eeeeeeee')
    return render(request, 'signup.html')


def login_page(request):

    try:

        if request.method=="POST":

            postData=request.POST
            first_name=postData.get("firstname")
            last_name=postData.get("lastname")
            phone=postData.get("phone")
            email=postData.get("email")
            password=postData.get("password")
            created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            customer_id=GenSequenceId("CUS")

            record = Customer.objects.get(email=email)
            request.session['customer_mobile'] = record.phone
            request.session['customer_id'] = record.customer_id
            request.session['user_name'] = record.first_name + " " + record.last_name
            print("login success")
        return render(request,'login.html')

    except Customer.DoesNotExist:
        print("Signup success")
        return render(request, 'signup.html')

    return render(request, 'login.html')


def dress_category(request,categoryID):
    print(type(categoryID))
    user_name=productdetails1=''
    try:
        user_name=request.session['user_name']
        customer_id=request.session['customer_id']

    except KeyError:
        request.session['user_name'] =''
        request.session['customer_id'] =''

    Cart_query = Cart.objects.filter(customer_id=customer_id)
    print(Cart_query,'Cart_query',len(Cart_query))
    cart_quanty=[]
    count_of_cart=0
    for i in Cart_query:
        cart_quanty.append(i.quantity)

    for num  in cart_quanty:
        count_of_cart += num
        print(count_of_cart,'yiuuyuy')


    categories = Category.objects.all()
    # categoryID = request.POST.get('categoryID')
    # print(categoryID,'categoryIDcategoryID')
    if categoryID:
        print(categoryID, 'If statement execurtteygygu')
        productdetails1 = ProductDetails.objects.filter(category_id_id=categoryID)
    else:
        print(categoryID, 'tyguijokpl[jh')
        productdetails1 = ProductDetails.objects.all()

    print(productdetails1,'productdetailssssssssss')

    context = {"categories":categories,'user_name': user_name,'count_of_cart':count_of_cart,"productdetails1":productdetails1}

    return render(request, 'dress_category.html',context)


def add_to_cart(request):

    user_name=product_items=total=''
    try:
        user_name=request.session['user_name']

    except KeyError:
        user_name = ''

    categories = Category.objects.all()
    Cart_items = Cart.objects.filter(user_name=user_name)
    print(Cart_items,'Cart_items',len(Cart_items))
    cart_quanty=[]
    count_of_cart=0
    for i in Cart_items:
        cart_quanty.append(i.quantity)

        product_items = ProductDetails.objects.get(product_id=i.product_id)
        i.product_name=product_items.product_name

    for num  in cart_quanty:
        count_of_cart += num
        print(count_of_cart,'yiuuyuy')

    print(user_name,'username')
    context={'Cart_items':Cart_items,'user_name':user_name,'count_of_cart':count_of_cart,'categories':categories}
    return render(request,'cart.html',context)


def UpdateItem(request):

    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(productId,action,'product id action')

    customer=request.session['user_name']
    customer_id=request.session['customer_id']
    product=ProductDetails.objects.get(product_id=productId)
    print(product.product_id,'product_id------',product.price,'product.price')

    # order,created=Order.objects.get_or_create(customer_id=customer)
    CartItem,created=Cart.objects.get_or_create(product_id=productId,customer_id=customer_id,price=product.price,user_name=customer,phone=request.session['customer_mobile'])

    if action=='add':
        print(action,'000')
        CartItem.quantity=(CartItem.quantity + 1)
        CartItem.total_price=int(product.price)*CartItem.quantity

    elif action=='remove':
        print(action, '000')
        CartItem.quantity = (CartItem.quantity - 1)
        CartItem.total_price = int(product.price) * CartItem.quantity

    CartItem.save()

    if CartItem.quantity <=0:

        CartItem.delete()

    return JsonResponse('Item was Added',safe=False)


def delete_view(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(productId,action,'product id action')
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Cart, product_id=productId)

    if request.method == "POST":
        # delete object
        obj.delete()

    return JsonResponse('Item was Deleted', safe=False)


def delete_view1(request):

    cart_id="CAR27M0232077"
    # obj = Cart.objects.raw('DELETE * FROM cart WHERE cart_id ="' + cart_id + '"')
    obj = Cart.objects.filter(cart_id=cart_id)

    for i in obj:
        id_1=i.id
        print(id_1)
        obj1 = Cart.objects.get(id=id_1)
        obj1.delete()
    return "0"


def checkout(request):

    user_name=product_items=total=billing_id=order_id=cart_id=''
    try:
        user_name=request.session['user_name']
        customer_id = request.session['customer_id']

    except KeyError:
        user_name = customer_id=''

    Customer_details = Customer.objects.get(customer_id=customer_id)
    categories = Category.objects.all()
    Cart_items = Cart.objects.filter(customer_id=customer_id).values()

    cart_quanty=[]
    cart_id_list=[]
    product_id_list=[]
    resultList=[]
    count_of_cart=0
    subtotal=0
    quantity_1=0
    if len(Cart_items)>0:
        for i in Cart_items:

            cart_id=i['cart_id']
            cart_id_list.append(cart_id)
            product_id_list.append(i['product_id'])
            subtotal += i['price'] * i['quantity']
            cart_quanty.append(i['quantity'])
            quantity_pric=str(i['price']) +" x "+str(i['quantity'])
            product_items = ProductDetails.objects.filter(product_id=i['product_id'])
            # print(product_items,'999999999999')

            for j in product_items:
                # print(j,'iiiiiiii')

                i['product_name'] = j.product_name

        for num  in cart_quanty:
            count_of_cart += num
        #     print(count_of_cart,'yiuuyuy')
        #
        # print(subtotal, '==>subtotal')
        # print(user_name,'username')

        shipping=100
        total=subtotal+shipping
    Billing_Details2 = Billing_Details.objects.filter(customer_id=customer_id).values()
    if len(Billing_Details2)>0:

        Billing_Details3 = Billing_Details2[0]
    else:
        Billing_Details3 = ''
    Order_Details = Order.objects.filter(customer_id=customer_id).values()
    Billing_Details1 = Billing_Details.objects.filter(customer_id=customer_id)
    print(Order_Details,'Order_Details')

    for bill_in in Billing_Details1:
        billing_id=bill_in.bill_id

    for order_d in Order_Details:
        order_id=order_d['order_id']

    context={'Cart_items':Cart_items,'user_name':user_name,'count_of_cart':count_of_cart,'categories':categories,'subtotal':subtotal,'total':total,'Customer_details':Customer_details,'Billing_Details2':Billing_Details3,"billing_id":billing_id,"resultList":resultList,"order_id":order_id,"cart_id":cart_id}

    # print(billing_id,"billing_id")
    if request.method=="POST" and request.POST.get("submit")=="Place Order":

        obj = Cart.objects.filter(cart_id=cart_id).delete()


        customer_id = customer_id
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        bill_address_line1 = request.POST.get('bill_address_line1')
        bill_address_line2 = request.POST.get('bill_address_line2')
        bill_country = request.POST.get('bill_Country')
        bill_city = request.POST.get('bill_city')
        bill_state = request.POST.get('bill_State')
        bill_pincode = request.POST.get('bill_Pincode')
        shipp_phone = request.POST.get('shipp_phone')
        shipp_email = request.POST.get('shipp_email')
        shipp_address_line1 = request.POST.get('shipp_address_line1')
        shipp_address_line2 = request.POST.get('shipp_address_line2')
        shipp_country = request.POST.get('shipp_Country')
        shipp_city = request.POST.get('shipp_City')
        shipp_state = request.POST.get('shipp_State')
        shipp_pincode = request.POST.get('shipp_Pincode')
        order_id=GenSequenceId("OD")

        BillItem = Billing_Details(customer_id=customer_id,first_name=first_name,last_name=last_name,phone=phone,email=email,
                                                           created_at=created_at,bill_address_line1=bill_address_line1,bill_address_line2=bill_address_line2,
                                                           bill_country=bill_country,bill_city=bill_city,bill_state=bill_state,bill_pincode=bill_pincode,
                                                           shipp_phone=shipp_phone,shipp_email=shipp_email,shipp_address_line1=shipp_address_line1,
                                                           shipp_address_line2=shipp_address_line2,shipp_country=shipp_country,shipp_city=shipp_city,shipp_state=shipp_state,
                                                           shipp_pincode=shipp_pincode,order_id=order_id
                                                           )

        BillItem.save()
        for row in Cart_items:

            product_quantity=row['quantity']
            product_price=row['price']
            cart_id=row['cart_id']
            product_id=row['product_id']
            sub_total_price=row['total_price']

            order_details=Order(sub_total_price=sub_total_price,total_price=total,quantity=product_quantity,product_price=product_price,cart_id=cart_id,product_id=product_id,order_id=order_id,customer_id=customer_id)
            order_details.save()


        return redirect('view_bill',order_id=order_id)

    return render(request,'checkout.html',context)


def view_bill(request,order_id):


    user_name=formated_date=billed_to=shipping_charges=total_price=''
    TOTAL_QUANTITY=SUB_TOTAL_PRICE=total_price1=0
    try:
        user_name=request.session['user_name']
        customer_id=request.session['customer_id']

    except KeyError:
        user_name=""
        customer_id=""
    # order_id="OD27M4447665"

    Billing_Detail={}
    Order_Details1 = Order.objects.filter(order_id=order_id).values()
    Billing_Details1 = Billing_Details.objects.filter(order_id=order_id).values()

    if len(Billing_Details1) >0:
        Billing_Details2=Billing_Details1[0]

        for i in Billing_Details1:

            bill_id=Billing_Details1[0]['bill_id']

            order_id=Billing_Details1[0]['order_id']
            billed_to=(i['first_name'])+" "+i['last_name']
            CreatedDate = i['created_at']
            date_time_obj = datetime.strptime(CreatedDate, '%d-%m-%Y %H:%M:%S')
            formated_date=datetime.strftime(date_time_obj, "%d-%m-%y")


    for y in Order_Details1:
        order_id = Billing_Details1[0]['order_id']
        product_names=ProductDetails.objects.filter(product_id=y['product_id'])
        print(product_names,'Product_Names')
        y['SHIP_TOTAL']=int(y['sub_total_price'])+int(y['shipping_charges'])
        TOTAL_QUANTITY += int(y['quantity'])
        SUB_TOTAL_PRICE += int(y['sub_total_price'])
        total_price1 += int(y['SHIP_TOTAL'])
        shipping_charges = int(y['shipping_charges'])
        total_price = int(y['total_price'])
        for j in product_names:
            y['PRODUCT_NAME']=j.product_name
    print(Order_Details1, 'Order_Details1')
    print(SUB_TOTAL_PRICE, 'SUB_TOTAL_PRICE')

    context = {'Billing_Details2':Billing_Details2,"formated_date":formated_date,"billed_to":billed_to,"Billing_Detail":Billing_Detail,'TOTAL_QUANTITY':TOTAL_QUANTITY,'SUB_TOTAL_PRICE':SUB_TOTAL_PRICE,'shipping_charges':shipping_charges,'total_price':total_price,'total_price1':total_price1,"Order_Details1":Order_Details1}
    return render(request, 'view_bill.html',context)


def intiate_payment(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    print(is_ajax,'issss')

    if is_ajax:
        if request.method=="POST":
            data = json.load(request)
            print(data, '1234567t890-')
            currency = 'INR'
            amount = 200  # Rs. 200

            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                               currency=currency,
                                                               payment_capture='0'))

            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']

            callback_url = '/paymenthandler/'
            print(callback_url,'***callback_url***')
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url

            return JsonResponse({'status': 'Valid request',"code":200,'context':context})

    return JsonResponse({'status': 'Invalid request',"code":400})


def Payment_pagw(request):
    print(request.POST,'pppppppppppppppppp')
    print(request.POST.get('razorpay_order_id'),'pppppppppppppppppp')
    currency = 'INR'
    if request.method=="POST":

        return render(request, 'index1.html')

    return JsonResponse({'status': 'Valid request',"code":200,'context':"context"})
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()


def Contact_Us(request):
    try:
        user_name=request.session['user_name']
        customer_id=request.session['customer_id']

    except KeyError:
        request.session['user_name'] = ''
        customer_id=''
    categories = Category.objects.all()

    Cart_items = Cart.objects.filter(customer_id=customer_id)
    print(Cart_items,'Cart_items',len(Cart_items))
    cart_quanty=[]
    count_of_cart=0
    for i in Cart_items:
        cart_quanty.append(i.quantity)

    for num  in cart_quanty:
        count_of_cart += num
        print(count_of_cart,'yiuuyuy')
    context={"count_of_cart":count_of_cart,"categories":categories}

    if request.method=="POST":
        print(request.POST)

    return render(request, 'contact.html',context)


def About_Us(request):
    try:
        user_name=request.session['user_name']
        customer_id = request.session['customer_id']

    except KeyError:
        user_name = customer_id=''


    categories = Category.objects.all()
    Cart_items = Cart.objects.filter(user_name=user_name)
    print(Cart_items,'Cart_items',len(Cart_items))
    cart_quanty=[]
    count_of_cart=0
    for i in Cart_items:
        cart_quanty.append(i.quantity)

        product_items = ProductDetails.objects.get(product_id=i.product_id)
        i.product_name=product_items.product_name

    for num  in cart_quanty:
        count_of_cart += num
        print(count_of_cart,'yiuuyuy')




    context={"categories":categories,'user_name':user_name,'customer_id':customer_id,'count_of_cart':count_of_cart}

    if request.method=="POST":
        print(request.POST)

    return render(request, 'about_us.html',context=context)


def Sendmail(request):
    try:
        customer_id=request.session['customer_id']

    except KeyError:
        customer_id= ''

    if request.method=="POST":
        print(request.POST)
        postData=request.POST
        name=postData.get("name")
        # phone=postData.get("phone")
        email=postData.get("email")
        subject=postData.get("subject")
        message=postData.get("message")
        customer_idd=customer_id
        created_at=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        Customer_Contact_Us = CustomerContactUs(name=name, email=email, subject=subject, message=message, customer_id=customer_idd,
                            created_at=created_at)



        subject = 'Thank You For Your Inquiry'
        message = 'Hi'+' '+name+', \n'+'Thank you for your interest in our products and services our Customer service executive will surely contact you \n In case of further inquiries, do not hesitate to let us know. \n\n  Kind regards,\nEshopper .'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

        Customer_Contact_Us.save()
        jsondata={
            "code":200,"msg":"success"}



    return JsonResponse(jsondata)


def submit_subscription_of_newsletter(request):
    print(request.POST,'REQUEST.POSTTTTT')
    try:
        customer_id=request.session['customer_id']

    except KeyError:
        customer_id= ''

    json_data={}

    if request.method=="POST":

        print(request.POST)
        postData = request.POST
        name = postData.get("name")
        # phone=postData.get("phone")
        email = postData.get("email")
        subject = postData.get("subject")
        message = postData.get("message")
        customer_idd = customer_id
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        try:
            subscribe_to_newsletter = Subscribe_to_NewsLetter.objects.get(email=email)
            json_data['msg']="Exists"

        except Subscribe_to_NewsLetter.DoesNotExist:



            subject = 'Thank You For Subscribing '
            message = "Hi "+name+"\n" \
            '''Thank you for Subscribing to our Newsletter.\n'''\
            '''You will receive our newsletter twice a month about Product updates, latest deals, and offers.'''\
            '''\nFeel free to reach out to us at service@gmail.com if you need any assistance.\n'''\
            "Regards Eshopper Team."
            print(message,'=======message')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)


            Customer_Contact_Us = Subscribe_to_NewsLetter(name=name, email=email, subject=subject, message=message, customer_id=customer_idd,
                                created_at=created_at)


            Customer_Contact_Us.save()
            json_data['msg'] = "Subscribtion Added"


    return JsonResponse(json_data)





def logout(request):
    request.session.clear()
    return redirect('/')


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

