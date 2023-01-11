from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<product_id>', views.product, name='product'),
    # path('supplier', views.supplier, name='supplier'),
    path('order', views.order, name='order'),
    path('orderConf/<order_id>', views.order_conf, name='orderConf'),
    # path('submit', views.submit, name='submit'),
    path('shopper', views.shopper, name='shopper'),
    path('basket', views.basket, name='basket'),
    path('basket/<product_id>', views.basket_add, name='basket_add'),
    path('item/<item_id>', views.item, name='item'),
    path('test', views.test, name='test'),
]
