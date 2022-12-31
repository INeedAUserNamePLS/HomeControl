from django.forms import ModelForm

from lights.models import Light


class LightForm(ModelForm):
    class Meta:
        model = Light
        fields = [
            'name', 'status', 'colour', 'brightness'
        ]
