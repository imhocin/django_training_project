from django.shortcuts import render, get_object_or_404
from .models import ProductsModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from pprint import pprint


# Create your views here.
def products_list_fb(request):

    products = ProductsModel.objects.all()

    context = {
        "title": "products list",
        "object_list": products,
    }
    return render(request, "products_list.html", context)


class ProductListView(ListView):

    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return ProductsModel.objects.all()


def product_details(request, id):

    # product = ProductsModel.objects.get(id=id)
    # product = get_object_or_404(ProductsModel, id=id)
    product = ProductsModel.objects.get_object_by_id(id)
    print(product)
    context = {
        "title": "Product Details",
        "product": product,
    }
    return render(request, "product_details.html", context)


class ProductDetails(DetailView):

    queryset = ProductsModel.objects.all()
    template_name = "product_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Product Details"
        return context

    def get_object(self, **kwargs):
        slug = self.kwargs.get("slug")
        product = ProductsModel.objects.get(slug=slug)
        return product


class ProductDetailsViewSlug(DetailView):

    queryset = ProductsModel.objects.filter()
    template_name = "product_details.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
