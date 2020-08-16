from django.urls import path

from . import views

app_name = 'leneva_backend'

urlpatterns = [
    path('', views.HomeView.as_view(), name='item'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('checkout/', views.checkout, name='checkout'),
]