from django.urls import path
from .views import GetItemView,AddItemView,GetItemTotalView,RemoveItemView

urlpatterns=[ 
    path('wishlist-item',GetItemView.as_view()),
    path('add-item',AddItemView.as_view()),
    path('get-item-total',GetItemTotalView.as_view()),
    path('remove-item',RemoveItemView.as_view()),
]















