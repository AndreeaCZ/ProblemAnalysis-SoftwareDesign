from django.db import models
import requests
from square.client import Client


TOKEN = 'Token b850eff5f1119dae5f82c8033ae0ce3754612037'
client = Client(access_token='EAAAELLHsnfKg1Khd1eP0nKAX4ltCD3be0-shbtYBNuH19unxZG52jRyXMGJRqH4', environment='sandbox')


class Product(models.Model):
    shop_code = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    EAN_13 = models.CharField(max_length=20)
    vat_rate = models.FloatField(default=0)
    price_in_cents = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def restock(self):
        orders = requests.get('https://rethink-supplier.herokuapp.com/order/', headers={'Authorization': TOKEN}).json()
        orderid = -1
        for order in orders:
            if not order['is_processed']:
                orderid = order['id']
                break
        if orderid != -1:
            print("Starting restock process for " + self.name)
            print('Using order with id ', orderid)
            requests.post('https://rethink-supplier.herokuapp.com/orderline/',
                          headers={'Authorization': TOKEN},
                          data={'product_id': self.shop_code, 'order_id': orderid, 'nr_of_products': 10})
            print('Added prod cu line')
            requests.post('https://rethink-supplier.herokuapp.com/send_order/',
                          headers={'Authorization': TOKEN},
                          data={'order_id': orderid})
            print('Sent order with id ', orderid)
            self.stock += 10
            self.save()
        else:
            requests.post('https://rethink-supplier.herokuapp.com/order/', headers={'Authorization': TOKEN})
            self.restock()


class Shopper(models.Model):
    name = models.CharField(max_length=200)


class Basket(models.Model):
    shopper = models.OneToOneField(Shopper, on_delete=models.CASCADE)

    def price(self):
        p = 0
        for item in self.item_set.all():
            p += item.product.price_in_cents *item.quantity
        return p

    def add_product(self, product_id):
        prod = Product.objects.get(id=product_id)
        item = self.item_set.filter(product=prod)
        if item.count() > 0:
            i = item.get(product=prod)
            i.quantity += 1
            i.save()
        else:
            i = self.item_set.create(product=prod)
            i.save()

    def order(self):
        o = self.shopper.order_set.create(total_price=self.price())
        o.save()
        for it in self.item_set.all():
            o.purchase_set.create(product=it.product, quantity=it.quantity)
            it.product.stock -= it.quantity
            it.product.save()
            if it.product.stock < 5:
                it.product.restock()
        return o

    def empty(self):
        self.item_set.all().delete()


class Item(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_price = models.IntegerField(default=0)


class Purchase(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
