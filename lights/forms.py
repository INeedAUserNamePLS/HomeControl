from django.forms import ModelForm
from lights.models import Light, Broker


class LightForm(ModelForm):
    class Meta:
        model = Light
        fields = ["status", "colour", "brightness"]


class AddForm(ModelForm):
    class Meta:
        model = Light
        fields = ["name"]


class BrokerForm(ModelForm):
    class Meta:
        model = Broker
        fields = ["server", "port", "keepAlive", "user", "password"]
