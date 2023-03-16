from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.

"""
By using the generics.CreateAPIView, we don't need to write the view code for 
processing the HTTP POST request and serializing the data manually. 
We can take advantage of Django REST Framework's built-in generic views
to handle these operations automatically.
"""
#Anything related to GenericAPIView : https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
class RoomView(generics.CreateAPIView):
    #Specifies the queryset that the view will use.
    queryset = Room.objects.all()
    #Specifies the serializer class that the view will use to serialize the incoming data
    serializer_class = RoomSerializer
