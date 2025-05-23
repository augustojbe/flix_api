from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializer import ActorSerializer


class ActorCresteListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Actor.objects.all()
  serializer_class = ActorSerializer
  
class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Actor.objects.all()
  serializer_class = ActorSerializer
  

