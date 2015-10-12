from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
#from django.core.mail import EmailMultiAlternatives
#from django.template import Context
#from django.template.loader import render_to_string

#import string, random
import logging
logger = logging.getLogger(__name__)

from .models import Category, Subcategory, Product, Cart, Order, Location
from .forms import CartForm


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(featured=True)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'category': category,
    }
    return render(request, 'category-page.html', context)


def subcategory(request, parent_category, slug):
    subcategory = Subcategory.objects.get(slug=slug)
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'subcategory-page.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'all-products.html', context)


def single_product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'product-page.html', context)


def all_locations(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
    }
    return render(request, 'all-locations.html', context)


def location(request, location_id):
    location = Location.objects.get(pk=location_id)
    context = {
        'location': location,
    }
    return render(request, 'location.html', context)


def add_to_cart(request, product_id):
    # check for authenticatino
    if request.user.is_authenticated():
        # get product by pk
        try:
            product = Product.objects.get(pk=product_id)
        # if it doesn't exist, nothing is added to cart
        except ObjectDoesNotExist:
            pass
        else:
            # if an active cart for this user already exists, get it
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            # if an active cart doesn't exist for this user, create it
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            # add product to cart
            cart.add_item_to_cart(product_id)
        # redirect user to their cart
        return redirect('cart')
    else:
        # if user is not authenticated, send them to the home page
        return redirect('home')


def remove_from_cart(request, product_id):
    # check for authentication
    if request.user.is_authenticated():
        # get product by pk
        try:
            product = Product.objects.get(pk=product_id)
        # if product does not exist, nothing to remove from cart
        except ObjectDoesNotExist:
            pass
        else:
            # get cart
            cart = Cart.objects.get(user=request.user, active=True)
            # remove product from cart
            cart.remove_item_from_cart(product_id)
        # redirect user to cart
        return redirect('cart')
    else:
        # redirect unauthenticated user to home page
        return redirect('home')


def cart(request):
    # check for authentication
    if request.user.is_authenticated():
        # get cart that was created in add_to_cart when an item was added
        cart = Cart.objects.filter(user=request.user.id, active=True)
        # orders are the items in the cart
        orders = Order.objects.filter(cart=cart)
        # instantiate order total with a dollar value of 0
        total = 0
        # instantiate quantity of items in order with a value of 0
        count = 0
        # loop through orders
        for order in orders:
            # for each product, add product price times product quantity to order
            total += order.quantity
            # for each product, increase order quantity by number of products ordered
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        # if user is not authenticated, redirect to home
        return redirect('home')


def checkout(request):
    if request.user.is_authenticated():
        cart = Cart.objects.get(user=request.user.id, active=True)
        items = Order.objects.filter(cart=cart)
        context = {
            'cart': cart,
            'items': items,
        }
        return render(request, 'store/checkout.html', context)
    else:
        return redirect('home')

def complete_order(request):
    if request.user.is_authenticated():
        cart = Cart.objects.get(user=request.user.id, active=True)
        cart.active = False
        cart.order_date = timezone.now()
        cart.save()
        return render(request, 'store/order-complete.html')
    else:
        return redirect('home')
