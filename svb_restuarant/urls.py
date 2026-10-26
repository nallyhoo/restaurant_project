"""
URL configuration for svb_restuarant project.

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
from django.contrib import admin
from django.urls import path
from myapp import views as svb_restuarant
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',svb_restuarant.index),
    path('about.html',svb_restuarant.about),
    path('service.html',svb_restuarant.service),
    path('index.html',svb_restuarant.index),
    path('signin.html',svb_restuarant.signin),
    path('menu.html',svb_restuarant.menu),
    path('booking.html',svb_restuarant.booking),
    path('team.html',svb_restuarant.team),
    path('testimonial.html',svb_restuarant.testimonial),
    path('contact.html', svb_restuarant.contact),
    path('shop.html',svb_restuarant.shop),
    path('checkout.html',svb_restuarant.checkout),
    path('shop-detail.html',svb_restuarant.shop_detail),
    path('cart.html',svb_restuarant.cart),
    path('order.html',svb_restuarant.Order),
    path('list_booking.html',svb_restuarant.Booking_list),
    path('add_product.html',svb_restuarant.Add1_product),
    path('update_product/', svb_restuarant.update_product),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
