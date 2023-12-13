from django import forms
from .models import Client


class NumeroClient(forms.ModelForm):
  class Meta:
    model = Client
    fields = ['numero']
    widgets = {
        'numero': forms.TextInput(attrs={'type': 'tel', 'class': 'input-style', 'placeholder': 'Votre numéro de téléphone'}),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['numero'].label = ''