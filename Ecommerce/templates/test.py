#1

l1=[23,56,89,77,45]
l2=[23,89,66,45]
list = []
print("The common elements are")
for i in l1:
  for j in l2:
    if i == j:
       list.append(i)
print(list)

#2

l1 = [-9, 45, -9, 7]
l2 = [3, -9,7,56]
print("The common elements are")
list1= set(l1).intersection(l2)
print(list1)




	**

						{% if user.is_authenticated %}

						{% if user.is_superuser == False %}
						<li class="nav-item">
							<a class="nav-link" href="{% url 'cart:cartview'%}"><img src="{% static 'images/cart.svg' %}"></a><sup class="mx-2 fs-5">{{c}}</sup>
						</li>
							<li class="nav-item">
								<a class="nav-link" href="{% url 'cart:orderview' %}">Your Orders</a>
							</li>


						{% else %}
						<li class="nav-item">
							<a class="nav-link" href="{% url 'shop:categories' %}">Add Categories</a>
						</li>
                       <li class="nav-item">
							<a class="nav-link" href="{% url 'shop:addproducts' %}">Add Products</a>
						</li>
                 {% endif %}


						 <li class="nav-item">
							 <a class="nav-link" href="{% url 'shop:userlogout' %}">Logout</a>
						 </li>
						<li class="nav-item">
							 <a class="nav-link" href="{% url 'shop:register' %}">Register</a>
						 </li>
                        <li class="nav-item">
							 <a class="nav-link" href="{% url 'shop:userlogin' %}">Login</a>
						 </li>


						{% endif %}
						</ul>



					<ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
						<li><a class="nav-link" href="#"><img src="{% static 'images/user.svg' %}"></a></li>
						<li><a class="nav-link" href="{% url 'cart:cartview'%}"><img src="{% static 'images/cart.svg' %}"></a><sup class="mx-2 fs-5">{{c}}</sup></li>
					</ul>



<ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
    <li>
        <a class="nav-link" href="#"><img src="{% static 'images/user.svg' %}"></a>
    </li>
    <li>
        <a class="nav-link" href="{% url 'cart:cartview' %}">
            <img src="{% static 'images/cart.svg' %}"><sup class="mx-2 fs-5">{{c}}</sup>
        </a>
    </li>
</ul>