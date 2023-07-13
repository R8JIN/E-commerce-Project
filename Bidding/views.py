from django.shortcuts import render, redirect, HttpResponse
from product.models import Product
from .models import WatchList, Bid, Cart, Order
from django.contrib import messages
import paypalrestsdk
from django.conf import settings
from paypalrestsdk import Payment


def create_payment(request, id):
    paypalrestsdk.configure(
        mode=settings.PAYPAL_MODE,
        client_id=settings.PAYPAL_CLIENT_ID,
        client_secret=settings.PAYPAL_CLIENT_SECRET
    )

    product = Product.objects.get(id=id)

    print(product)
    payment = Payment({
        'intent': 'sale',
        'payer': {
            'payment_method': 'paypal'
        },
        'redirect_urls': {
            'return_url': 'http://localhost:8000/biddingpayment/execute/%s'% id,
            'cancel_url': 'http://localhost:8000/payment/cancel/'
        },
        'transactions': [{
            'amount': {
                'total': product.final_price,
                'currency': 'USD'
            },
            'payee': {
                'email': 'rojin1234@gmail.com'
            },
            "description": f"This is the payment transaction for  ."}
        ]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == 'approval_url':
                redirect_url = link.href
                return redirect(redirect_url)
    else:
        return render(request, 'payment_failed.html')


def execute_payment(request, id):
    print(request.user)
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    paypalrestsdk.configure(
        mode=settings.PAYPAL_MODE,
        client_id=settings.PAYPAL_CLIENT_ID,
        client_secret=settings.PAYPAL_CLIENT_SECRET
    )
    payment = Payment.find(payment_id)
    if payment.execute({'payer_id': payer_id}):
        p = Product.objects.get(id=id)
        # Payment executed successfully

        order = Order(user=request.user, product=Product.objects.get(id=id),
                      price=p.final_price)
        cart_ob = Cart.objects.get(product=Product.objects.get(id=id))
        cart_ob.status = 'Paid'
        cart_ob.save()
        order.save()
        messages.success(request, "Payment Done")
        return render(request, 'Payment.html', {})
    else:
        return HttpResponse('Payment execution failed.')


def watchlist(request):
    products = WatchList.objects.filter(user=request.user).order_by('-datetime')
    # print(products)
    return render(request, 'WatchList.html', {'products': products})


def view_invoice(request, id):
    return render(request, 'ProductInvoice.html', {})

def add_to_watchlist(request, id):
    product = WatchList.objects.filter(user=request.user).filter(product_id=id)
    if not product:
        product = WatchList(product=Product.objects.get(id=id), user=request.user)
        product.save()
        messages.success(request, 'Added to your watchlist')
    else:
        messages.warning(request, 'Already exist in your watchlist')
    return redirect('Home')


def remove_from_watchlist(request, id):
    product = WatchList.objects.filter(user=request.user).filter(id=id)
    product.delete()
    messages.success(request, 'Removed from the watchlist')
    return redirect('Home')


def add_bid(request, id):
    product = Product.objects.get(id=id)
    print(type(id))
    if request.user == product.user:
        messages.warning(request, 'You are the auctioneer')
        return redirect('http://localhost:8000/product/%s' % id)
    else:
        if request.method == 'POST':
            amount = request.POST['amt']
            b = Bid.objects.filter(product__id=id)
            if not b:
                if float(amount) < float(product.price)+10/100*float(product.price):
                    messages.error(request, f'Bid amount should be more than {product.price}')
                    return redirect('http://localhost:8000/product/%s' % id)
            else:
                if float(amount) < b.last().bid_amt + 10/100*float(b.last().bid_amt):
                    messages.error(request, f'Bid amount should be more than bid amount Rs. {b.last().bid_amt}')
                    return redirect('http://localhost:8000/product/%s' % id)
            bid = Bid(user=request.user, product=Product.objects.get(id=id), bid_amt=amount)
            bid.save()
            messages.success(request, 'Bid submitted')
    return redirect('Home')


def cart(request):
    add_cart()
    product = Cart.objects.filter(user=request.user)
    order = Order.objects.filter(user=request.user)
    print(product)
    return render(request, 'Cart.html', {'product': product, 'order': order})


def add_cart():
    products = Product.objects.all()
    for p in products:
        ctime = p.remaining_time_in_minutes()
        if ctime == 0:
            bid = Bid.objects.filter(product__id=p.id)
            # print(bid)
            if bid:
                bid = bid.last()
                print(bid.bid_amt)
                p.final_price = bid.bid_amt;
                p.save()
                print(bid.product.id)
                c = Cart.objects.filter(user=bid.user).filter(product__id=bid.product.id)
                if not c:
                    c = Cart(user=bid.user, product=Product.objects.get(id=bid.product.id))
                    c.save()






