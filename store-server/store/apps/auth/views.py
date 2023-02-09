from django.shortcuts import render


# Create your views here.
def checkout(request):
    return render(request, 'auth/checkout.html')


def login(request):
    return render(request, 'auth/login.html')
