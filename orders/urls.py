from .views import *
from django.urls import path 

urlpatterns = [
   path("make_order/<int:id>/", make_order, name="make_order"),

]