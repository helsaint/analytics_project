from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from emissions.models import Emissions, Countries
from django.core import serializers
from django_pivot.pivot import pivot
from django.db.models import Sum
from json import dumps

def emissions_pivot_data(request):
    dataset_gdp = Emissions.objects.values('country').order_by(
        'country').annotate(total_gdp=Sum('gdp'))
    dataset_iso = Emissions.objects.values('iso_code').annotate(total_gdp=Sum('gdp'))
    dataset_countries = Countries.objects.values('alpha_3', 'alpha_2')
    lst_dataset_iso = list(dataset_iso)
    lst_dataset_countries = list(dataset_countries)
    dict_dataset_countries = dict()
    for l in lst_dataset_countries:
        dict_dataset_countries[l['alpha_3']] = l['alpha_2']
    
    dict_gdp = dict()
    for l in lst_dataset_iso:
        if l['iso_code'] in dict_dataset_countries:
            str_account_value = int(l['total_gdp']/1000000)
            dict_gdp[dict_dataset_countries[l['iso_code']]] = str_account_value
    json_gdp = dumps(dict_gdp)

    return render(request,'emissions_with_pivots.html',{'emissions_pivot': dataset_gdp, 
    'gdpData1': json_gdp})
