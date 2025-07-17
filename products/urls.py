from django.urls import path
from . import views

urlpatterns = [
    path("fb", views.products_list_fb, name="products_list_fb"),
    path("cb", views.ProductListView.as_view(), name="ProductListView"),
    path("details-fb/<id>", views.product_details, name="product_details"),
    path("details-cb/<slug>", views.ProductDetails.as_view(), name="ProductDetails"),
    path(
        "details-cb-slug/<slug>",
        views.ProductDetailsViewSlug.as_view(),
        name="ProductDetailsViewSlug",
    ),
]
