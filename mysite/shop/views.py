from django.shortcuts import render
from django.views import generic
from .models import Product, Order

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


class OrderListView(generic.ListView):
    model = Order
    context_object_name = 'orders'
    template_name = "orders.html"

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class OrderDetailView(generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = "order.html"



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "product"