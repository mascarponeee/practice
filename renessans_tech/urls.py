from django.urls import path
from .views import fun1

urlpatterns = [
    path('', fun1)
]
