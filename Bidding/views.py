from django.shortcuts import render, redirect
from product.models import Product
from .models import WatchList, Bid, Cart
from django.contrib import messages
# Create your views here.


def watchlist(request):
    product = WatchList.objects.all()
    return render(request, 'WatchList.html', {'product': product})


def add_to_watchlist(request, id):
    product = WatchList.objects.filter(user=request.user).filter(id=id)
    if not product:
        product = WatchList(user=request.user, product=Product.objects.get(id=id))
        product.save()
        messages.success(request, 'Added to your watchlist')
    else:
        messages.warning(request, 'Already exist in your watchlist')

    return redirect('Home')


def add_bid(request, id):
    product = Product.objects.get(id=id)
    if request.user == product.user:
        messages.warning(request, 'You are the auctioneer')
        return redirect('/')
    else:
        if request.method == 'POST':
            amount = request.POST['amt']
            b = Bid.objects.filter(product__id=id)
            if not b:
                if float(amount) < float(product.price):
                    messages.error(request, f'Bid amount should be more than {product.price}')
                    return redirect('/')
            else:
                if float(amount) < b.last().bid_amt:
                    messages.error(request, f'Bid amount should be more than bid amount Rs. {b.last().amount}')
                    return redirect('/')
            bid = Bid(user=request.user, product=Product.objects.get(id=id), bid_amt=amount)
            bid.save()
            messages.success(request, 'Bid submitted')
        return redirect('Home')


def cart(request):
    product = Cart.objects.filter(user=request.user)
    return render(request, 'Cart.html', {'product': product})



def add_cart():
    products = Product.objects.all()

    for p in products:
        ctime = p.remaining_time_in_minutes()
        if ctime == 0:
            bid = Bid.objects.filter(product__id=p.id)
            # print(bid)
            if bid:
                bid = bid.last()
                print(bid.product.id)
                cart = Cart.objects.filter(user=bid.user).filter(product__id=bid.product.id)
                if not cart:
                    cart = Cart(user=bid.user, product=Product.objects.get(id=bid.product.id))
                    cart.save()

add_cart()



