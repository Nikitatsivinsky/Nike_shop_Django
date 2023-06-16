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


class ItemReviewForm(forms.Form):
    stars = forms.ChoiceField(
        label='Ваша оцінка',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'stars'}))
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': '1', 'placeholder': 'Відгук'}))



