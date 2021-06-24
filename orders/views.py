from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

# Create your views here.
from products.models import Product
from .forms import OrderForm
from .models import Order


@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(feature=True)
    if not qs.exists():
        return redirect("/")
    product = qs.first()
    # if not product.has_inventory:
    #     return redirect("/no-inventory")
    user = request.user
    order_id = request.session.get("order_id")  # cart
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None

    if order_id == None:
        new_creation = True
        order_obj = Order.objects.create(product=product, user=user)
        request.session['order_id'] = order_obj.id
    if order_obj != None and new_creation == False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product, user=user)
    request.session['order_id'] = order_obj.id

    # ???
    form = OrderForm(request.POST or None, product=product, instance=order_obj)
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get(
            "shipping_address")  # or instance
        order_obj.billing_address = form.cleaned_data.get("billing_address")
        order_obj.mark_paid(save=False)
        # order_obj.status = 'paid'  I can use this and call mark_paid on post_save at models
        order_obj.save()
        del request.session['order_id']

        return redirect("/success")

    return render(request, 'orders/checkout.html', {"form": form, "object": order_obj})