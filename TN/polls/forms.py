from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('originplace', 'outboundpartialdate', 'destinationplace', 'inboundpartialdate','telephone','adults')
        widgets = {
            'outboundpartialdate': forms.DateInput(format='%Y-%m-%d',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'inboundpartialdate': forms.DateInput(format='%Y-%m-%d',
                                                   attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                          'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))