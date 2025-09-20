from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Contact,Sign_up,Chef , Booking ,Online_order
from django.contrib.auth import authenticate, login
from django.db.models import Sum

#API


# Create your views here.
def index(request):
    products = Product.objects.all()
    chefs = Chef.objects.all()
    contacts = Contact.objects.all()
    context = {
        'products': products,
        'chefs': chefs,
        'contacts': contacts,
        }
    return render(request,'index.html',context)

def about(request):
    Chefs = Chef.objects.all()

    return render(request,'about.html',{'chefs':Chefs})

def service(request):
    return render(request,'service.html')



def menu(request):
    products = Product.objects.all()
    return render(request,'menu.html',{'products': products})

def booking(request):
    context ={}
    if request.method=='POST':
        name = request.POST.get('name_booking')
        em = request.POST.get('email_booking')
        datetime = request.POST.get('date_time')
        people = request.POST.get('booking_people')
        req = request.POST.get('special_request')
        
        obj = Booking(name=name ,email=em , date =datetime ,quantity_peo=people ,special_req=req)
        obj.save()
        context['message']= f' hey {name} your booking will be approve soon!'
    return render(request,'booking.html',context)

def team(request):
    chefs = Chef.objects.all()
    
    return render(request,'team.html',{'chefs': chefs})


def testimonial(request):
    contacts = Contact.objects.all()
    return render(request,'testimonial.html',{'contacts': contacts})


def signin(request):

    context={}
    if request.method=="POST":
        if "signup" in request.POST:
            # SignUp logic
            em=request.POST.get('email')
            name=request.POST.get('username1')
            pas=request.POST.get('password')
            cfpass=request.POST.get('cfpassword')

            if cfpass == pas:
                obj=Sign_up(username=name , email=em,password=pas)
                obj.save()
                context['message']=f'Hey {name} you Have Signup sucessfully !'
            else:
                context['message'] = "Passwords do not match. Please try again."
        elif "login" in request.POST:
            # SignIn logic
            name = request.POST.get('username1')
            pas = request.POST.get('password')

            try:
                user = Sign_up.objects.get(username=name, password=pas)
                context['message'] = f'Welcome back {user.username}!'
                return redirect('shop.html', context)
            except Sign_up.DoesNotExist:
                context['message'] = "Invalid username or password."
                context['mode'] = "login"


    return render(request, 'signin.html', context)

    
        
    
        
        

def contact(request):
    context={}
    if request.method=="POST":
        name = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msz = request.POST.get('message')
        
        obj= Contact(name = name,email=em,subject=sub ,message =msz)
        obj.save()
        context['message']=f'Dear {name} Thank you for you Contact we will response soon!'
        
        
        
    return render(request,'contact.html',context)

def shop(request):
    products = Product.objects.all()
    return render (request,'shop.html', {'products': products} , )
def checkout(request):
    return render(request,'checkout.html')

def shop_detail(request):
    online_orders = Online_order.objects.all().order_by('-created_at')
    total_revenue = online_orders.aggregate(total=Sum('total_price'))['total'] or 0
    total_orders = online_orders.count()
    average_order = total_revenue / total_orders if total_orders > 0 else 0
    context={
        'online_orders': online_orders,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'average_order': average_order,
    }
    return render(request,'shop-detail.html',context)

def cart(request):
    return render(request,'cart.html')


def Order(request):
    products =Product.objects.all()

    if request.method == 'POST':
        # Get form data
        fname = request.POST.get('Fullname_Order')
        phone_num = request.POST.get('phone_numberOrder')
        address = request.POST.get('Address_Order')
        special = request.POST.get('Special_Order')

        # Get cart data from JSON
        import json
        cart_data = request.POST.get('cart_data', '[]')
        try:
            cart_items = json.loads(cart_data)
        except:
            cart_items = []

        # Calculate total and create order items
        total_price = 0
        order_items = []

        for item in cart_items:
            product = Product.objects.get(id=item['id'])
            quantity = item['quantity']
            item_total = float(product.price) * quantity
            total_price += item_total
            order_items.append(f"{product.name} (x{quantity})")

        # Create order record
        product_names = ", ".join(order_items)
        obj = Online_order(
            product_name=product_names,
            quantity_order=len(cart_items),
            total_price=str(total_price),
            fullname=fname,
            phone_number=phone_num,
            address_delivery=address,
            special_order=special
        )
        obj.save()

        # Return success response
        return render(request, 'order.html', {
            'products': products,
            'success': True,
            'order_id': obj.id,
            'message': f'Order placed successfully! Order ID: #{obj.id}'
        })

    return render(request, 'order.html', {'products': products})

def Booking_list(request):
    bookings = Booking.objects.all()
    return render(request,'list_booking.html',{'bookings':bookings})

