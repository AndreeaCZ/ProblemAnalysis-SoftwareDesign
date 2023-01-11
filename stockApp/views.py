from django.shortcuts import render
import requests
import environ
from stockApp.models import Product, Shopper, Basket, Item, Order
from square.client import Client


TOKEN = 'Token b850eff5f1119dae5f82c8033ae0ce3754612037'
SHOPPER = Shopper.objects.get(id=1)
BASKET = Basket.objects.get(id=1)
client = Client(access_token='EAAAELLHsnfKg1Khd1eP0nKAX4ltCD3be0-shbtYBNuH19unxZG52jRyXMGJRqH4', environment='sandbox')


def test(request):
    result = client.payments.list_payments()
    if result.is_success():
        print(result.body['payments'][0])
    elif result.is_error():
        print(result.errors)


def index(request):
    prods = Product.objects.all()
    return render(request, 'core/index.html', {"prods": prods})


def product(request, product_id):
    prod = Product.objects.get(id=product_id)
    return render(request, 'core/product.html', {'product': prod, 'baskets': BASKET})


# def supplier(request):
#     response = requests.post('https://rethink-supplier.herokuapp.com/order/', headers={'Authorization': TOKEN})
#     prods = response.json()
#     return render(request, 'core/index.html', {'info': prods[0]['id']})


def order(request):
    o = BASKET.order()
    requests.post('http://localhost:3000/fromDjango?price=' + str(BASKET.price()) + '&order=' + str(o.id))
    BASKET.empty()
    return order_conf(request, o.id)


def order_conf(request, order_id):
    o = Order.objects.get(id=order_id)
    return render(request, 'core/order.html', {'order': o})


def shopper(request):
    return render(request, 'core/shopper.html', {'shopper': SHOPPER})


def basket(request):
    return render(request, 'core/basket.html', {'basket': BASKET})


def basket_add(request, product_id):
    prod = Product.objects.get(id=product_id)
    BASKET.add_product(product_id)
    return render(request, 'core/basketAdd.html', {'basket': BASKET, 'product': prod})


def item(request, item_id):
    it = Item.objects.get(id=item_id)
    return render(request, 'core/item.html', {'item': it})


# Used this to load products into db
# def submit(request):
#     response = requests.get('https://rethink-supplier.herokuapp.com/product/', headers={'Authorization': TOKEN})
#     prods = response.json()
#     for prod in prods:
#         p = Product.objects.get(shop_code=prod['id'])
#         p.vat_rate = prod['vat_rate']
#         p.price_in_cents = prod['price_in_cents']
#         p.save()
