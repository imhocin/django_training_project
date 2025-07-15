from django.urls import path
from . import views

urlpatterns = [
    path("fb", views.products_list_fb, name="products_list_fb"),
    path("cb", views.ProductListView.as_view(), name="ProductListView"),
]
