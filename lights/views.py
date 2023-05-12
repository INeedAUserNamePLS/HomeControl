import json
from django.http import JsonResponse
import paho.mqtt.client as mqtt_client
from . import mqtt
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseRedirect
from lights.forms import LightForm, AddForm
from lights.models import Light
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # adding lamp
        # create a form instance and populate it with data from the request:
        form = AddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            light = form.save(commit=False)
            light.save()
        return redirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        light_list = Light.objects.all()
        context = {'latest_light_list': light_list}
        return render(request, 'lights/index.html', context)


@login_required
def detailLight(request, light_id):
    # if this is a POST request we need to process the form data
    light_instance = Light.objects.get(pk=light_id)
    if request.method == 'POST':
        # editing existing lamp
        # create a form instance and populate it with data from the request:
        form = LightForm(request.POST, instance=light_instance)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            light = form.save(commit=False)
            light.save()
            # send mqtt
            data = {'name': light.name, 'status': light_instance.status, 'colour': light_instance.colour,
                    'brightness': light_instance.brightness}
            mqtt_client.Client.publish(mqtt.client, 'lights', json.dumps(data))
            # redirect to a new URL:
            return HttpResponseRedirect('/lights/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LightForm(initial={'status': light_instance.status, 'colour': light_instance.colour,
                                  'brightness': light_instance.brightness})
        try:
            light = Light.objects.get(pk=light_id)
        except Light.DoesNotExist:
            raise Http404("Light does not exist")
        return render(request, 'lights/detail.html', {'form': form, 'light': light})
    return HttpResponseRedirect('/lights/')

@login_required
def addLight(request):
    form = AddForm()
    return render(request, 'lights/add.html', {'form': form})

@login_required
def deleteLight(request, light_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        Light.objects.filter(pk=light_id).delete()
    return HttpResponseRedirect('/lights/')

@login_required
def editBroker(request):
    return render(request,'broker/detail.html', {})