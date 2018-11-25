from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = [ 'status']
        widgets = {
            'submitted': forms.DateInput(attrs={'class':'datepicker'}),
        }