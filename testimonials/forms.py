from django import forms
from captcha.fields import ReCaptchaField


class TestimonialForm (forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    captcha = ReCaptchaField()
