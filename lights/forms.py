from django.forms import ModelForm

from lights.models import Light


class LightForm(ModelForm):
    class Meta:
        model = Light
        fields = [
            'status', 'colour', 'brightness'
        ]


class AddForm(ModelForm):
    class Meta:
        model = Light
        fields = [
            'name'
        ]
