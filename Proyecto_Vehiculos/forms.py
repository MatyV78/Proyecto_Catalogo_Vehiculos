from django import forms
from django.contrib.auth.models import User
from Proyecto_Vehiculos.models import Vehiculo, VehiculoElec, VehiculoUsado, Marca, Modelo, Comentario, ComentarioUso, ComentarioElec
import re

class RegistroSimpleForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña",
        help_text="Debe tener al menos 6 caracteres y una mayúscula o un número."
    )
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r"[A-Z]", password):
            raise forms.ValidationError("Debe contener al menos una letra mayúscula.")
        if not re.search(r"[0-9]", password):
            raise forms.ValidationError("Debe contener al menos un número.")
        if not re.search(r"[-]", password):
            raise forms.ValidationError("Debe contener al menos un guion (-).")
        return password


# --------- FORMULARIOS EXISTENTES DE TU PROYECTO ---------
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["marca", "modelo", "año", "tipo_vehiculo", "Precio"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }


class VehiculoElecForm(forms.ModelForm):
    class Meta:
        model = VehiculoElec
        fields = ["marca", "modelo", "año", "tipo_vehiculo", "Precio"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }


class VehiculoUsadoForm(forms.ModelForm):
    class Meta:
        model = VehiculoUsado
        fields = ["marca", "modelo", "año", "tipo_vehiculo", "Precio"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_vehiculo": forms.Select(attrs={"class": "form-control"}),
            "Precio": forms.TextInput(attrs={"class": "form-control"}),
        }


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre_marca", "informacion_marca"]
        widgets = {
            "nombre_marca": forms.TextInput(attrs={"class": "form-control"}),
            "informacion_marca": forms.TextInput(attrs={"class": "form-control"}),
        }


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ["marca", "modelo", "año"]
        widgets = {
            "marca": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "año": forms.TextInput(attrs={"class": "form-control"}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ComentarioUsoForm(forms.ModelForm):
    class Meta:
        model = ComentarioUso
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ComentarioElecForm(forms.ModelForm):
    class Meta:
        model = ComentarioElec
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
