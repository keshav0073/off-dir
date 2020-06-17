from django import forms

class Contactform(forms.Form):
    first_name =forms.CharField(widget=forms.TextInput(attrs={'class':'medium',}), required=True)
    last_name =forms.CharField(widget=forms.TextInput(attrs={'class':'medium',}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'medium'}),required=True)
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'medium',}), required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea medium',}), required=True)