from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_response, name="coffee"),
]
