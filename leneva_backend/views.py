from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.utils import timezone
from django.shortcuts import redirect
from .models import Item, OrderItem, Order
from django.contrib import messages

# Create your views here.
class HomeView(ListView):
    model=Item
    template_name="home-page.html"

class ProductDetailView(DetailView):
    model=Item
    template_name="product-page.html"


def checkout(request):
    context={
        'items':Item.objects.all()
    }

    return render(request,"checkout-page.html",context)

def add_to_cart(request, slug):
    item=get_object_or_404(Item,slug=slug)
    item.inside_cart = True
    item.save()
    order_item,created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    print(OrderItem.objects.filter(quantity=1))
    orders = Order.objects.filter(user=request.user,ordered=False)
    print("----------------------this",orders)
    if orders.exists():
        order=orders[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request, "Item Quantity has been updated!")
        else:
            messages.info(request, "Item Added to your Order!")
            order.items.add(order_item)
    else:
        ordered_date=timezone.now()
        order = Order(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item Added to your Order!")
    return redirect("leneva_backend:product",slug=slug)

def remove_from_cart(request, slug):
    item=get_object_or_404(Item,slug=slug)
    item.inside_cart = False
    item.save()
    orders = Order.objects.filter(user=request.user,ordered=False)
    if orders.exists():
        order=orders[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item,created = OrderItem.objects.get_or_create(
                item=item,
                user=request.user,
                ordered=False
            )
            order.items.remove(order_item)
            messages.info(request, "This item has been removed!")
            return redirect("leneva_backend:product",slug=slug)
        else:
            messages.info(request, "Item does not exist in CART!")
            return redirect("leneva_backend:product",slug=slug)
    else:
        messages.info(request, "Item does not exist in CART!")
        return redirect("leneva_backend:product",slug=slug)