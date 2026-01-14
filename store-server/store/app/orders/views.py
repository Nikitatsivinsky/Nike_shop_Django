from django.shortcuts import render


def cart(request):
    return render(request, 'orders/cart.html')


def confirmation(request):
    return render(request, 'orders/confirmation.html')


def tracking(request):
    return render(request, 'orders/tracking.html')
