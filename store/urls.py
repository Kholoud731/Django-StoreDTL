from django.urls import path
from .views import all_products, one_product, category_product

app_name = 'store'

urlpatterns = [
    path('', all_products, name='all_products'),
    path('item/<int:id>', one_product, name='one_product'),
    path('search/<str:name>', category_product, name='category_product'),
]
