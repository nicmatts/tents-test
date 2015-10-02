from django.shortcuts import render

from .models import Category, Subcategory, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
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
