from django.urls import path
from Bidding.views import add_to_watchlist, add_bid, watchlist, cart, add_cart, create_payment, execute_payment
from .views import *
urlpatterns = [
    path('add_watchlist/<id>', add_to_watchlist, name='watchlist'),
    path('bid/<id>', add_bid, name='bid'),
    path('watchlist', watchlist, name='watch'),
    path('cart', cart, name='cart'),
    path('remove/<id>', remove_from_watchlist, name='remove_watch'),
    path('add_cart', add_cart, name='add_cart'),
    path('payment/create/<id>', create_payment, name='payment'),
<<<<<<< HEAD
    path('payment/execute/<uid>/<id>', execute_payment, name='execute_payment'),
    path('invoice/<id>', view_invoice, name='invoice'),
    path('deposite/create/<id>', create_deposite, name='deposite'),
    path('deposite/execute/<id>', execute_deposite, name='execute_deposite'),
=======
    path('payment/execute/<id>', execute_payment, name='execute_payment'),
    path('invoice/<id>', view_invoice, name='invoice')
>>>>>>> f8b31dd233eacae95b4fa5b9f2294677fd88df5b
    # path('cancel-payment/', cancel_payment, name='cancel_payment'),

]