from django.forms import ModelForm
from .models import Todomo

class TodomoForm(ModelForm):
    class Meta:
        model = Todomo
        fields = ['title', 'memo', 'important']

