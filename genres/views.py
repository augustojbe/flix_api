from rest_framework import generics
from genres.models import Genre
from genres.serializer import GenereSerializer


class GenreCreateListView(generics.ListCreateAPIView):
  queryset = Genre.objects.all()
  serializer_class  = GenereSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenereSerializer

