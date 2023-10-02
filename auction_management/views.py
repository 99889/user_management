
from rest_framework import generics, permissions
from .models import Auction
from .serializers import AuctionSerializer

class AuctionListCreateView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuctionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticated]
