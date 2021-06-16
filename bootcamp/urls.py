"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from products.views import (
    # bad_view,
    product_create_view,
    product_detail_view,
    product_api_detail_view,
    search_view,
    product_list_views
)

urlpatterns = [
    path('search/', search_view),
    #path('bad-view-dont-use/', bad_view),
    path('products/<int:pk>/', product_detail_view),
    path('products/', product_list_views),
    path('products/create/', product_create_view),
    # path('products/1/', views.product_detail_view),
    # path('api/products/<int:id>/', views.product_api_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view),
    path('admin/', admin.site.urls),
]
