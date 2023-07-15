from django.contrib import admin
from .models import WatchList, Bid, Order, Cart, Deposite

# Register your models here.
admin.site.register(WatchList)
admin.site.register(Bid)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Deposite)