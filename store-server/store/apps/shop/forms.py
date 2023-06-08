from django import forms
from apps.auth.models import MailDistribution




class SubscribeForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Ваша Пошта"}))

    class Meta:
        model = MailDistribution
        fields = ['email']


class ItemFiltrationForm(forms.Form):
    search_input = forms.CharField(label='',
                                   widget=forms.TextInput(attrs={'class': "form-control",
                                                                 'id': "search_input",
                                                                 'placeholder': "Впишіть назву товару"}))
