from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializer import ReviewSerializer
from app.permissions import GlobalDefaultPermission


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  
class ReviweRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  