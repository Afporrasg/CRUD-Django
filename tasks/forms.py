from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'titulo', 'descripcion', 'deadline', 'importante', 'completada']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control mb-3', 'placeholder': 'Ingrese una descripción'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control form-control mb-3', 'type': 'datetime-local', 'placeholder': 'Seleccione una fecha y hora'})
        }
       

