from django.urls import path
from product.views import home, product_detail, bid_so_far, sell, category
urlpatterns = [
    path('', home, name='Home'),
    # path('product', product_view),
    path('product/<id>', product_detail, name='Prod_view'),
    path('bid_so_far/<id>', bid_so_far, name='bidsofar'),
    path('sell/', sell, name='sell'),
    path('category/<id>', category, name='category')
]