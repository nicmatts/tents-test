from django.shortcuts import render

from .models import Category, Subcategory


def home(request):
    return render(request, 'home.html')


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
