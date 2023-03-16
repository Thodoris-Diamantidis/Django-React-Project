from django.urls import path
from .views import RoomView

"""In Django, views are called as functions when a request is made to the associated URL.
 However, when using class-based views in Django, we need to convert the class-based view
   to a function-based view before it can be called in the URL configuration. 
   This is where the .as_view() method comes into play."""
urlpatterns = [
    path('', RoomView.as_view())
]