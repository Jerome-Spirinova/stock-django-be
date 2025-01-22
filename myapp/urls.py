from django.urls import path
from .views import CategoryListCreateView, ExpensiveProductView, FeaturedProductView, ProductListCreateView, UpdateStockView

urlpatterns = [
    path('api/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/product/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/expensive/', ExpensiveProductView.as_view(), name='expensive-product'),
    path('api/products/featured/', FeaturedProductView.as_view(), name='featured-product'),
    path('api/products/update-stocks/', UpdateStockView.as_view(), name='update-stocks'),
]