from django.urls import path
from . import views


urlpatterns = [
    path('', views.emissions_pivot_data, name='emissions_pivot_data'),
]