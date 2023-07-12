from django.urls import path
from .views import *

urlpatterns = [
    path('', count_view, name='count_view'),
]
