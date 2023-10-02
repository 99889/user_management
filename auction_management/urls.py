from django.urls import path
from . import views

urlpatterns = [
    path('auctions/', views.AuctionListCreateView.as_view(), name='auction-list-create'),
    path('auctions/<int:pk>/', views.AuctionRetrieveUpdateDestroyView.as_view(), name='auction-retrieve-update-destroy'),
    
]
