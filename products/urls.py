from .views import *
from django.urls import path , include
urlpatterns = [
    path("list/", list, name="product_list"),
    path("get/<int:id>/", get, name="product_get"),
    path("add/", add_page, name="add_page"),
    path("add_action/", add_action, name="add_action"),
    path("remove/<int:id>/", remove, name="remove"),
    path("update/<int:id>/", update_page, name="update_page"),
    path("update_action/", update_action, name="update_action"),
]
