from django.shortcuts import render
from .models import ProductsModel
from django.views.generic.list import ListView


# Create your views here.
def products_list_fb(request):

    products = ProductsModel.objects.all()

    context = {
        "title": "products list",
        "products": products,
    }
    return render(request, "products_list.html", context)


class ProductListView(ListView):

    queryset = ProductsModel.objects.all()
    template_name = "products_list.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
