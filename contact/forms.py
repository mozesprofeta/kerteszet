from django import forms
from captcha.fields import ReCaptchaField   


class ContactForm (forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    telephone = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(attrs={'theme': 'clean'})
