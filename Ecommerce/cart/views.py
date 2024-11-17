import razorpay
from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart
from django.contrib.auth.decorators import login_required
import razorpay
from cart.models import Payment
from cart.models import Orderdetails
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.models import User


# Create your views here.
@login_required
def addtocart(request,p):
    u=request.user
    pr=Product.objects.get(id=p)
    try:
         c=Cart.objects.get(user=u,product=pr)
         if(pr.stock>0):
             c.quantity+=1
             c.save()
             pr.stock-=1
             pr.save()
    except:
        if (pr.stock>0):
             c=Cart.objects.create(user=u,product=pr,quantity=1)
             c.save()
             pr.stock-=1
             pr.save()
    return redirect('cart:cartview')

def cartview(request):

    u=request.user
    total=0
    c=Cart.objects.filter(user=u)
    for i in c:
        total+=i.quantity*i.product.price
    context={'cart':c,'total':total}
    return render(request,"addcart.html",context)

@login_required()
def cartremove(request,p):
    u=request.user
    p=Product.objects.get(id=p)
    try:
        c=Cart.objects.get(user=u,product=p)
        if(c.quantity>1):
            c.quantity-=1
            c.save()
            p.stock+=1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save()
    except:
        pass
    return redirect('cart:cartview')

@login_required()
def cartdelete(request,p):
    u=request.user
    p=Product.objects.get(id=p)
    try:
        c = Cart.objects.get(user=u,product=p)
        c.delete()
        p.stock+=c.quantity
        p.save()
    except:
        pass
    return redirect('cart:cartview')


def orderform(request):
    if(request.method=="POST"):
        address=request.POST['ad']
        phone=request.POST['ph']
        pin=request.POST['pin']
        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product.price
        total1=int(total*100)
        client=razorpay.Client(auth=('rzp_test_799mLSNLvO1DOV','zZhjWppBFyvsXjKpSSQy2UKK'))      #creates a client connection
        response_payment=client.order.create(dict(amount=total1,currency="INR"))     #create an order with razorpay
        print(response_payment)
        order_id=response_payment['id']
        status=response_payment['status']
        if(status=="created"):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()
            for i in c:
                o=Orderdetails.objects.create(product=i.product,user=u,no_of_items=i.quantity,address=address, phone=phone,pin=pin,order_id=order_id)
                o.save()
        response_payment['name']=u.username
        context={'payment':response_payment}
        return render(request,'payment.html',context)

    return render(request, 'orderform.html')

@csrf_exempt
def paymentstatus(request,u):
    user = User.objects.get(username=u)
    if not request.user.is_authenticated:
        login(request,user)
    if(request.method == "POST"):
        response=request.POST
        print(response)
        param_dict={
            'razorpay_order_id':response['razorpay_order_id'],
            'razorpay_payment_id':response['razorpay_payment_id'],
            'razorpay_signature':response['razorpay_signature']
              }
    client = razorpay.Client(auth=('rzp_test_799mLSNLvO1DOV', 'zZhjWppBFyvsXjKpSSQy2UKK'))
    print(client)
    try:

           status=client.utility.verify_payment_signature(param_dict)
           print(status)
           p=Payment.objects.get(order_id=response['razorpay_order_id'])
           p.razorpay_payment_id=response['razorpay_payment_id']
           p.paid=True
           p.save()

           o=Orderdetails.objects.filter(order_id=response['razorpay_order_id'])
           print(o)
           for i in o:
               i.payment_status="completed"
               i.save()

           c=Cart.objects.filter(user=user)
           c.delete()

    except:
            pass

        # print(u)
    return render(request,'paymentstatus.html',context={'status':status})

def orderview(request):
    u=request.user
    o=Orderdetails.objects.filter(user=u)
    print(o)
    context={'orders':o}
    return render(request,"orderview.html",context)