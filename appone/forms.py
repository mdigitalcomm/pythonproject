from django.forms import ModelForm
from appone.models import Website


class MyModelform(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
