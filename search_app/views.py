from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


# Create your views here.

def Search(request):
    products = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=Query) | Q(description__contains=Query))
        return render(request, 'search.html', {'Query': Query, 'products': products})




