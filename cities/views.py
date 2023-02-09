from django.shortcuts import render
from django.http import JsonResponse
from cities.models import Cities
from django.core import serializers

def cities_with_pivot(request):
    return render(request,'cities_with_pivots.html',{})

def cities_pivot_data(request):
    dataset = Cities.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data,safe=False)


# Create your views here.
