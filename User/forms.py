from django import forms
from . models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model= User
        fields = ['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}, render_value=True),
        } 