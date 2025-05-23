from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializer import GenereSerializer


class GenreCreateListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Genre.objects.all()
  serializer_class  = GenereSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Genre.objects.all()
  serializer_class = GenereSerializer

