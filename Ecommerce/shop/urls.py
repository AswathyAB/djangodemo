"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from shop import views

app_name="shop"

urlpatterns = [
    path('',views.categories,name="categories"),
    path('products/<int:p>',views.products,name="products"),
    path('productdetails/<int:p>',views.productdetails,name="productdetails"),
    path('register/',views.register,name="register"),
    path('login/',views.userlogin,name="userlogin"),
    path('logout/',views.userlogout,name="userlogout"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('addstock/<int:p>',views.addstock,name="addstock"),
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)