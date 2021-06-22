from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from products.models import Product
from .models import Order


@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(feature=True)
    if not qs.exists():
        return redirect("/")
    product = qs.first()
    user = request.user
    Order.objects.create(product=product, user=user)
    return render(request, 'forms.html', {})
