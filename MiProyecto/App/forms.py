from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput 
from django.contrib.auth.forms import AuthenticationForm
from .models import Categoria, Comida, Adicional, Guarnicion, Bebida, Postre, CafeTe, Mesa

class Crear_Comida_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    precio = forms.FloatField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

class Crear_Categoria_forms(forms.Form):
    nombre = forms.CharField(max_length=50)

class Crear_Adicional_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()

class Crear_Comida_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    precio = forms.FloatField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

class Crear_Guarnicion_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()

class Crear_Bebida_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()

class Crear_Postre_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()

class Crear_CafeTe_forms(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()

class Crear_Mesa_forms(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero_mesa','sector']


class Crear_Pedido_forms(forms.Form):
    mesa = forms.ModelChoiceField(queryset=Mesa.objects.all())
    plato_principal = forms.ModelChoiceField(queryset=Comida.objects.all())
    adicional_plato_principal = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False)
    guarnicion = forms.ModelChoiceField(queryset=Guarnicion.objects.all(), required=False)
    adicional_guarnicion = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False)
    bebida = forms.ModelChoiceField(queryset=Bebida.objects.all())
    adicional_bebida = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False)
    postre = forms.ModelChoiceField(queryset=Postre.objects.all(), required=False)
    adicional_postre = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False)
    cafe_te = forms.ModelChoiceField(queryset=CafeTe.objects.all(), required=False)
    adicional_cafe_te = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False)
    entregado = forms.BooleanField(required=False)

class Crear_Pedido_Cliente_Forms(forms.Form):
    mesa = forms.ModelChoiceField(queryset=Mesa.objects.all(), label='Mesa')
    plato_principal = forms.ModelChoiceField(queryset=Comida.objects.all(), label='Plato Principal')
    adicional_plato_principal = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False, label='Adicional Plato Principal')
    guarnicion = forms.ModelChoiceField(queryset=Guarnicion.objects.all(), required=False, label='Guarnición')
    adicional_guarnicion = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False, label='Adicional Guarnición')
    bebida = forms.ModelChoiceField(queryset=Bebida.objects.all(), label='Bebida')
    adicional_bebida = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False, label='Adicional Bebida')
    postre = forms.ModelChoiceField(queryset=Postre.objects.all(), required=False, label='Postre')
    adicional_postre = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False, label='Adicional Postre')
    cafe_te = forms.ModelChoiceField(queryset=CafeTe.objects.all(), required=False, label='Café/Té')
    adicional_cafe_te = forms.ModelChoiceField(queryset=Adicional.objects.all(), required=False, label='Adicional Café/Té')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password1', 
            'password2'
        ]
        help_texts = {k:'' for k in fields}

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget = PasswordInput())