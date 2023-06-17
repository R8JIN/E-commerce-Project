from django.shortcuts import render, redirect
from product.models import Product, Category
from Bidding.models import Bid
# Create your views here.


def home(request):
    products = Product.objects.all().order_by('category', '-datetime')
    category = Category.objects.all()
    print(products)
    content = {'products': products, 'category': category}
    return render(request, 'index.html', content)


# def product_view(request):
#
#     return render(request, 'index.html', {'products': products})

def bid_so_far(request, id):
    bid = Bid.objects.filter(product__id=id).order_by('-datetime')
    return render(request, 'Sell.html', {'bid':bid})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    bid = Bid.objects.filter(product__id=id).order_by('-datetime')
    b = bid.last()
    ctime = product.remaining_time_in_minutes()
    return render(request, 'Product.html', {'product': product, 'ctime': ctime, 'bid': bid, 'b': b})

# def sell(request):
#     if request.method == 'POST':
#         title = request.POST[]
#         category = request.POST[]
#         price = request.POST[]
#         description = request.POST[]
#         thumbnails = request.POST[]
#         images = request.POST[]

#         counter = request.POST[]
#
#         product = Product(title=title, category=Category.objects.get(title=category)
#                           , price=price, description=description, thumbNails=thumbnails
#                           ,images = images, duration_in_minutes=counter, state=Product.STATE.RUNNING)
#         product.save()
#
#         return redirect('Home')
#
#     return render(request, 'Sell.html', {})
