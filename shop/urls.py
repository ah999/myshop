from django.conf.urls import url
from . import views


app_name = 'shop'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='product_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='product_details'),

]


