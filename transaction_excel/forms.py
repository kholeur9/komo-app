from django import forms
from .models import ExcelInput

class ExcelInputForm(forms.ModelForm):
    class Meta:
        model = ExcelInput
        fields = ('extract_data',)
        widgets = {
            'extract_data': forms.FileInput(attrs={'multiple': True, 'class': 'input-file', 'id': 'extract'}),
        }
        
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['extract_data'].label = ''