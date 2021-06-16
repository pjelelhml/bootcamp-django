from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Product
from products.forms import ProductModelForm

# Create your views here.


# def bad_view(request, *kargs, **kwargs):
#     print(request.GET)
#     my_request_data = dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == "true":
#         print("new product")
#         Product.objects.create(title=my_request_data.get('title')[0],
#                                content=my_request_data.get('content')[0])
#     return HttpResponse("Dont do this")


def search_view(request, *args, **kwargs):  # /search/
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    query = request.GET.get('q')  # q
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "abc", "query": query}
    return render(request, "home.html", context)


# def product_create_view(request, *args, **kwargs):
#     print(request.POST)
#     print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get("title"))
#                 title_from_input = my_form.cleaned_data.get("title")
#                 Product.objects.create(title=my_form.cleaned_data.get("title"))
#             print("post_data", post_data)
#     return render(request, "forms.html", {})

@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do some stuff
        # obj.user = request.user
        obj.save()

        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)

        # Product(**data)
        form = ProductModelForm()
        # return HttpResponseRedirect("/success")
        # return Redirect("/success")
    return render(request, "forms.html", {"form": form})


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
