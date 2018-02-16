from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post-item/', views.cpost_item_view.as_view(), name="post-item"),
    path('item-<int:pk>/', views.item_detail_view.as_view(), name='item-detail'),
    path('item-search/', views.priceView, name='price-view')
]