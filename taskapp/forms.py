from .models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = [ 'status']
        widgets = {
            'submitted': forms.DateInput(attrs={'class':'datepicker'}),
        }


class RollNOForm(UserCreationForm):
    coursename = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','first_name',  'coursename', 'password1', 'password2', )