from django import forms
from apps.auth.models import MailDistribution


class SubscribeForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Ваша Пошта"}))

    class Meta:
        model = MailDistribution
        fields = ['email']
