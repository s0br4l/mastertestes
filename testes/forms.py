from django import forms
from django.forms import ModelForm
from .models import Medidasteste

class MedidasForm(ModelForm):
    class Meta:
        model = Medidasteste
        fields = ('nome', 'peso', 'estatura', 'Ptronco', 'Pcintura', 'Pabdomen', 'Pquadril', 'PantebracoD', 'PbracoD', 'PcoxaD', 'PpernaD')

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selecione o nome'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em kg'}),
            'estatura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Ptronco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pcintura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pabdomen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pquadril': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PantebracoD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PbracoD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PcoxaD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PpernaD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
        }


class TetesForm(ModelForm):
    class Meta:
        model = Medidasteste
        fields = ('nome', 'Ir_vir', 'Dinamometro', 'Sentar_levantar', 'Marcha')

        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selecione o nome'}),
            'Ir_vir': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Dinamometro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em kgf'}),
            'Sentar_levantar': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de repetições'}),
            'Marcha': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'})
        }
