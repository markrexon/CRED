from django.forms import ModelForm
from .models import Infant

class Forms(ModelForm):
    class Meta:
        model=Infant
        fields = '__all__'