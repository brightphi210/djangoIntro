
from django.urls import path 

from .views import *

urlpatterns = [
    path('', home, name='homename'),
    path('delete/<str:pk>/', deleteTask, name='remove'),
    path('update/<str:pk>/', updateTask, name='update')
]
