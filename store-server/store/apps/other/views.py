from django.shortcuts import render


def contact(request):
    return render(request, 'other/contact.html')


def elements(request):
    return render(request, 'other/elements.html')
