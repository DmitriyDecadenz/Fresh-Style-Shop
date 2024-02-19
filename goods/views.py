from django.shortcuts import render
from goods.models.categories import Category
from goods.models.goods import Product


def category(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"title": "Catalog", "categories": categories, "products": products}

    return render(request, "goods/goods.html", context)
