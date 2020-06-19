from django.contrib import messages
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView,DetailView
from .models import Item ,OrderItem ,Order
from django.utils import timezone

def checkout(request):
    return render(request, "checkout.html")

class HomeView(ListView):
    model = Item
    paginate_by = 1
    template_name="home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name="product.html"

def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    order_item,created = OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            messages.info(request,"This item was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("core:product",slug=slug)

def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed to your cart")
            return redirect("core:product", slug=slug)
        else:
            # Add a message sayin user doesn't have that orderItem
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        #Add a message sayin user doesn't have an order
        messages.info(request, "You donot have an active order")
        return redirect("core:product", slug=slug)






