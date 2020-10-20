from django.views import generic
from .models import Product, Category
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'shop/products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'shop/products/details.html'

