from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from lights.models import Light


def index(request):
    latest_light_list = Light.objects.order_by('name')[:5]
    context = {'latest_light_list': latest_light_list}
    return render(request, 'lights/index.html', context)


def detail(request, light_id):
    try:
        light = Light.objects.get(pk=light_id)
    except Light.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lights/detail.html', {'light': light})
