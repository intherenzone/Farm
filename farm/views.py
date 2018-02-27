from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    farm_list = Farm.objects.all()
    context = {'farm_list': farm_list}
    return render(request, 'farm/index.html', context)

def detail(request, farm_id):
    try:
        farm = Farm.objects.get(pk=farm_id)
    except Farm.DoesNotExist:
        raise Http404("Farm does not exist")
    return render(request, 'farm/detail.html', {'farm': farm})
