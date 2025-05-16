from django.forms import ModelForm
from .models import models
from .models import *
class register_form(ModelForm):
    
    class Meta:
        model = register
        fields = ("__all__")
