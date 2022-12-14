from django.urls import path
from .views import ListOrderView,ListOrderDetailView

app_name="orders"

urlpatterns=[ 
    path('get-order',ListOrderView.as_view()),
    path('get-order/<transactionId>',ListOrderDetailView.as_view())
]









