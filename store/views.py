from django.shortcuts import render

from .models import Category


def home(request):
    return render(request, 'home.html')


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)
