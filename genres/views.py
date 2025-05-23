from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializer import GenereSerializer
from app.permissions import GlobalDefaultPermission


class GenreCreateListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermission)
  queryset = Genre.objects.all()
  serializer_class  = GenereSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermission)
  queryset = Genre.objects.all()
  serializer_class = GenereSerializer

