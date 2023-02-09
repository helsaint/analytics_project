from django.urls import path
from . import views

urlpatterns = [
    path('', views.cities_with_pivot, name='cities2_with_pivot'),
    path('data', views.cities_pivot_data, name='cities2_pivot_data'),
]