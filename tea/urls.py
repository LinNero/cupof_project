from django.urls import path
from . import views

urlpatterns = [
    path('', views.tea_response, name="tea"),
]