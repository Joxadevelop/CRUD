from django.urls import path
from .views import Index, CreateCategoryView, CreateProductView, ProductDetail, UpdeteProductView, DeleteProductView, ProductListView
urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('add-cat/', CreateCategoryView.as_view(), name='add_cat'),
    path('add/', CreateProductView.as_view(), name='add'),
    path('detail/<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('updete/<slug:slug>/', UpdeteProductView.as_view(), name='update'),
    path('delete/<slug:slug>/', DeleteProductView.as_view(), name='delete'),
    path('', Index.as_view(), name='index')
]