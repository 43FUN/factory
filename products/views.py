from django.shortcuts import render
from products.models import Products, Category


def categories(request, category_id=1):
    category = Category.objects.get(id=category_id)
    products = Products.objects.filter(category_id=category_id)
    return render(request, 'categories.html',
                  {'products': products, 'category': category})


def product(request, products_id=1):
    product = Products.objects.get(id=products_id)
    return render(request, 'product.html', {'product': product})
