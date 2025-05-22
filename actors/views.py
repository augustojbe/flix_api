from rest_framework import generics
from actors.models import Actor
from actors.serializer import ActorSerializer


class ActorCresteListView(generics.ListCreateAPIView):
  queryset = Actor.objects.all()
  serializer_class = ActorSerializer
  
class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Actor.objects.all()
  serializer_class = ActorSerializer
  

