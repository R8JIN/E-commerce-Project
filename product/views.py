from django.shortcuts import render, redirect
from django.contrib import messages
from product.models import Product, Category
<<<<<<< HEAD
from Bidding.models import Bid, WatchList, Deposite
=======
from Bidding.models import Bid, WatchList
>>>>>>> f8b31dd233eacae95b4fa5b9f2294677fd88df5b
from Content.models import Ads
# Create your views here.


def home(request):
    products = Product.objects.all().order_by('category','-datetime')
    ads = Ads.objects.all()
    carousel = Product.objects.all().order_by('-datetime')
    category = Category.objects.all()
    # /print(products)
    content = {'ads': ads, 'products': products, 'category': category, 'carousel': carousel}
    return render(request, 'index.html', content)


def category(request, id):
    products = Product.objects.filter(category=Category.objects.get(id=id)).order_by('datetime')
    category = Category.objects.get(id=id)
    return render(request, 'Category.html', {'products': products, 'category': category})
# def product_view(request):
#
#     return render(request, 'index.html', {'products': products})


def bid_so_far(request, id):
<<<<<<< HEAD
    bid = Bid.objects.filter(product__id=id).order_by('-datetime__time')
=======
    bid = Bid.objects.filter(product__id=id).order_by('bid_amt').reverse()
>>>>>>> f8b31dd233eacae95b4fa5b9f2294677fd88df5b
    return render(request, 'BidSofar.html', {'bid': bid})


def product_detail(request, id):
    product = Product.objects.get(id=id)
<<<<<<< HEAD
    bid = Bid.objects.filter(product__id=id).order_by('-datetime')
    try:
        deposite = Deposite.objects.get(user=request.user)
    except:
        deposite = None
    watchlist = WatchList.objects.filter(product=product)
=======
    bid = Bid.objects.filter(product__id=id).order_by('bid_amt').reverse()
    watchlist = WatchList.objects.filter(product=product)
    print(watchlist)
>>>>>>> f8b31dd233eacae95b4fa5b9f2294677fd88df5b
    b = bid.first()
    ctime = product.remaining_time_in_minutes()
    context = { 'watch':watchlist, 'product': product, 'ctime': ctime, 'bid': bid, 'b': b}
    return render(request, 'Product.html', context )


def sell(request):
    category = Category.objects.all()
    if request.method == 'POST':
        title = request.POST["title"]
        categ = request.POST["Category"]
        price = request.POST["price"]
        description = request.POST['desc']
        thumbnails = request.FILES['thumb']
        images = request.FILES['Image']

        counter = int(request.POST['duration'])

        product = Product(title=title, category=Category.objects.get(id=categ), user=request.user
                          , price=price, description=description, thumbNails=thumbnails
                          ,images=images, duration_in_minutes=counter*60,
                          state=Product.STATE.RUNNING)
        product.save()
        messages.success(request, 'Product added to Auction')
        return redirect('Home')
#
    return render(request, 'Sell.html', {'category': category})
