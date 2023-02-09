from django.shortcuts import render
from django.http import JsonResponse
from cities2.models import Cities2
from django.core import serializers

def cities2_with_pivot(request):
    return render(request,'cities2_with_pivots.html',{})

def cities2_pivot_data(request):
    dataset = Cities2.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data,safe=False)
# Create your views here.
