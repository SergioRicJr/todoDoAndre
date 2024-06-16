from django import forms
from .models import TaskEntity

class TaskForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateTimeField()
    completed = forms.BooleanField(required=False)

class TaskUpdateForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    due_date = forms.DateTimeField(required=False)
    completed = forms.BooleanField(required=False)