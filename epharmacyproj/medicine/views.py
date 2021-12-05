from django.shortcuts import render, HttpResponse,redirect
from math import ceil
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from datetime import datetime
from django.contrib import messages
from .models import Product, Cart, Customer, Contact, OrderPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def medicine_store(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/index.html',{'totalitem':totalitem})

# class ProductDetailView(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         return render(request, 'medicine/productdetail.html', {'product': product}) 

class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        # ye product cart main already exist karta han current login user ka n agar exists nahi hoga toh False main jaega
        if request.user.is_authenticated:
            # for show how many items in cart in cart icon
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'medicine/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})

class CovidDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        corona = Product.objects.get(pk=pk)
        item_already_in_cart = False
        # ye product cart main already exist karta han current login user ka n agar exists nahi hoga toh False main jaega
        if request.user.is_authenticated:
            # for show how many items in cart in cart icon
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=corona.id) & Q(user=request.user)).exists()
        return render(request, 'medicine/coviddetail.html', {'corona': corona, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})
        

class OxygenDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        oxy = Product.objects.get(pk=pk)
        item_already_in_cart = False
        # ye product cart main already exist karta han current login user ka n agar exists nahi hoga toh False main jaega
        if request.user.is_authenticated:
            # for show how many items in cart in cart icon
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=oxy.id) & Q(user=request.user)).exists()
        return render(request, 'medicine/oxydetail.html', {'oxy': oxy, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})

def covid(request, data=None):
    totalitem = 0
    if data == None:
        covid = Product.objects.filter(category='COVID')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/covid.html', {'covid': covid,'totalitem':totalitem})

def oxygen(request, data=None):
    totalitem = 0
    if data == None:
        Oxygen = Product.objects.filter(category='OXY')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/oxygen.html', {'Oxygen': Oxygen,'totalitem':totalitem})

def dermatology(request, data=None):
    totalitem = 0
    if data == None:
        derma = Product.objects.filter(category='DERMA')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/dermatology.html', {'derma': derma,'totalitem':totalitem})

def diabetes(request, data=None):
    totalitem = 0
    if data == None:
        diab = Product.objects.filter(category='DIAB')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, 'medicine/diabetes.html',{'diab':diab, 'totalitem':totalitem})

def depression(request, data=None):
    totalitem = 0
    if data == None:
        dep = Product.objects.filter(category='DEP')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user)) 
    return render(request, 'medicine/depression.html',{'dep':dep, 'totalitem':totalitem})

def dental(request,data=None):
    totalitem = 0
    if data == None:
        den = Product.objects.filter(category='DEN')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user)) 
    return render(request, 'medicine/dental.html',{'den':den, 'totalitem':totalitem})

def fracture(request, data=None):
    totalitem = 0
    if data == None:
        fra = Product.objects.filter(category='FRAC')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, 'medicine/fracture.html',{'fra':fra, 'totalitem':totalitem})

def eyecare(request, data=None):
    totalitem = 0
    if data == None:
        eye = Product.objects.filter(category='EYE')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/eye.html',{'eye':eye, 'totalitem':totalitem})

def womenscare(request, data=None):
    totalitem = 0
    if data == None:
        women = Product.objects.filter(category='WOM')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/womenscare.html',{'women':women, 'totalitem':totalitem})

def hairfall(request, data=None):
    totalitem = 0
    if data == None:
        hair = Product.objects.filter(category='HAIR')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, 'medicine/hairfall.html',{'hair':hair, 'totalitem':totalitem})

def blood(request, data=None):
    totalitem = 0
    if data == None:
        blood = Product.objects.filter(category='BP')
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))     
    return render(request, 'medicine/blood.html',{'blood':blood, 'totalitem':totalitem})

def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))   
    return render(request, 'medicine/about.html',{'totalitem':totalitem})

def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    # agar koi form post hua than
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        # for save in db
        contact.save()
        messages.success(request, 'Your message has been sent! We will get back to you within 24 Hrs')
    return render(request, 'medicine/contact.html',{'totalitem':totalitem})

def privacy(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/privacy.html',{'totalitem':totalitem})

def searchMatch(query, item):
    # return true only if query matches the item
    if query in item.med_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    # totalitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        # agar kuch bhi product na ho toh
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'medicine/search.html', params)    


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    mydata = Cart(user=user, product=product)
    mydata.save()
    return redirect('/cart')

# jo user han uske cart main jo data han ussi ke data ko hi dikahana hn
def show_cart(request):
    totalitem = 0
    # user hamara authenticated han ya nahi
    if request.user.is_authenticated:
        # for show how many items in cart in cart icon
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        # jo user login han ussi ka cart dikhao
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        # p.user means pehle product ka user n jo user ne login kiya han toh woh object p main rakh diya jaega
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'medicine/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount, 'totalitem': totalitem})
        # if cart is empty
        else:
            return render(request, 'medicine/emptycart.html')   

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)                 

@login_required
def checkout(request):
    totalitem = 0
    # current user
    user = request.user
    # jo current user login han ussi ka hi address dikahana chaiye
    add = Customer.objects.filter(user=user)
    # now for cart items jo user login ussi ka hi cart items dikahao
    cart_items = Cart.objects.filter(user=user)
    # now i want to see the total amount in checkout page
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'medicine/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items, 'totalitem': totalitem})

# when order is placed by clicking on continue in checkout page than customer id will save n cart items will save in db (order_placed) n cart main jo item han woh delete vhi hona chaiye n for loop we use becaz cart main multiple items hoga toh 1 by 1 karke order placed hoga db main
@login_required
def payment_done(request):
    user = request.user
    # custid we write name in input type radio
    # yeh custid jo humne banaya han name dekar checkout main jo address main customer ka naam likha han ye usse refer kar raha han
    custid = request.GET.get('custid')
    # customer ka id
    customer = Customer.objects.get(id=custid)
    # woh product jo cart main han
    cart = Cart.objects.filter(user=user)
    for c in cart:
        order = OrderPlaced(user=user, customer=customer,
                            product=c.product, quantity=c.quantity).save()
        # order.save()
        c.delete()
    return redirect("orders")

@login_required
def orders(request):
    totalitem = 0
     # current user ka order placed dikaho
    orderplaced = OrderPlaced.objects.filter(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/orders.html', {'orderplaced': orderplaced,'totalitem':totalitem})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'medicine/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered Sucessfully')
            form.save()
        return render(request, 'medicine/customerregistration.html', {'form': form})


@login_required
def address(request):
    totalitem = 0
    add = Customer.objects.filter(user=request.user)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'medicine/address.html', {'add': add, 'active': 'btn btn-primary','totalitem':totalitem})

# if person is login than they access that page
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'medicine/profile.html', {'form': form, 'active': 'btn btn-primary','totalitem':totalitem})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            # current user
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'medicine/profile.html', {'form': form, 'active': 'btn btn-primary'})
