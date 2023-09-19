from django.urls import path
from . import views
app_name = 'shop'


urlpatterns = [
    path('', views.all_prod_cat, name="allProdCat"),
    path('<slug:c_slug>/', views.all_prod_cat, name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/', views.prod_detail, name="product_detail"),

]