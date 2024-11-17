from django.shortcuts import render,redirect
from shop.models import Itemcategory
from shop.models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def categories(request):
    c=Itemcategory.objects.all()
    context={'cat':c}
    return render(request,"category.html",context)

def products(request,p):
    c=Itemcategory.objects.get(id=p)
    p = Product.objects.filter(category=c)
    context = {'cat': c, 'pr': p}
    return render(request,'product.html',context)

def productdetails(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,"productdetails.html",context)

def register(request):
     if (request.method == "POST"):
         u = request.POST['u']
         p = request.POST['p']
         cp = request.POST['cp']
         f = request.POST['f']
         l = request.POST['l']
         e = request.POST['e']
         if (p == cp):
            user=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            user .save()
            return redirect('shop:categories')

     return render(request, 'register.html')

def userlogin(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('shop:userlogin')

@csrf_exempt
def addproducts(request):
    if (request.method=="POST"):
         n=request.POST['n']
         i=request.FILES.get('i')
         d=request.POST['d']
         s=request.POST['s']
         p=request.POST['p']
         c=request.POST['c']
         cat=Itemcategory.objects.get(name=c)

         p=Product.objects.create(name=n,image=i,description=d,stock=s,price=p,category=cat)
         p.save()
         return redirect('shop:categories')

    return render(request, 'addproducts.html')


def addcategory(request):
     if (request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        i=request.FILES['i']
        c=Itemcategory.objects.create(name=n,description=d,image=i)
        c.save()
        return redirect('shop:categories')
     return render(request,'addcategory.html')
    # return render(request,'addcategory.html')

def addstock(request,p):
    product=Product.objects.get(id=p)
    if (request.method=="POST"):
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:productdetails',p)
    context={'pro':product}
    return render(request,"addstock.html",context)
