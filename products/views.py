from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.


def home_view(request, *args, **kwargs):  # /search/
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    context = {"name": "Justin"}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id {obj.pk}")

    # if obj.content == None:
    #     return render(request, "products/detail.html", ,
    #                   {"object": obj})

    return render(request, "products/detail.html", {"object": obj})


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})

    return JsonResponse({"id": obj.pk})


def product_list_views(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


# class HomeView():
#     pass
