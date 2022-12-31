import json
from django.http import JsonResponse
#from mqtt.mqtt import client as mqtt_client
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from lights.forms import LightForm
from lights.models import Light


def index(request):
    light_list = Light.objects.all()
    context = {'latest_light_list': light_list}
    return render(request, 'lights/index.html', context)


def detail(request, light_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            light = form.save(commit=False)
            light.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/lights/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LightForm()
        try:
            light = Light.objects.get(pk=light_id)
        except Light.DoesNotExist:
            raise Http404("Light does not exist")
        return render(request, 'lights/detail.html', {'form': form, 'light': light})
    return HttpResponseRedirect('/lights/')


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            light = form.save(commit=False)
            light.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/lights/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LightForm()
    return render(request, 'lights/add.html', {'form': form})


def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})
