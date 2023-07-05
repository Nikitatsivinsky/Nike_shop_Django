from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
# from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib import messages

# from django.views import View

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def checkout(request):
    return render(request, 'user/checkout.html')


class MyLoginView(LoginView):
    template_name = 'user/register.html'
    redirect_authenticated_user = False
    next_page = '/'



class RegistrationView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        for errors in form.errors.items():
            for error_message in errors[1]:
                messages.error(self.request, error_message)
        return super().form_invalid(form)
    def form_valid(self, form):
        password1 = form.cleaned_data['password1']
        password2 = form.data['password2']
        email = form.data['email']
        username = form.cleaned_data['username']

        if password1 != password2:
            messages.error(self.request, "Паролі не співпадають.")
            return self.form_invalid(form)

        email_in_db = User.objects.filter(email=email).exists()
        login_in_db = User.objects.filter(username=username).exists()

        if email_in_db:
            messages.error(self.request, "Ця пошта вже зареестрованна.")
            return self.form_invalid(form)
        elif login_in_db:
            messages.error(self.request, "Цей логін вже зареестрованний.")
            return self.form_invalid(form)

        if self.register_new_user(username, email, password1):
            messages.success(self.request, "Ви успішно зареєструвалися!")
        else:
            messages.success(self.request, "Відбулася помилка! Спробуйте пізніше!")
        return super().form_valid(form)

    def register_new_user(self, username, email, password):
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return True
        except Exception as ex:
            print(ex)
            return False

# class RegistrationView(View):
#     template_name = 'user/register.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('/')
#
#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             confirmpassword = form.cleaned_data['confirmpassword']
#             email = form.cleaned_data['email']
#             login = form.cleaned_data['username']
#
#             if password != confirmpassword:
#                 messages.error(request, "Паролі не співпадають.")
#                 return render(request, self.template_name, {'form': form})
#
#             email_in_db = User.objects.filter(email=email).exists()
#             login_in_db = User.objects.filter(username=login).exists()
#
#             if email_in_db:
#                 messages.error(request, "Ця пошта вже зареестрованна.")
#                 return render(request, self.template_name, {'form': form})
#             elif login_in_db:
#                 messages.error(request, "Цей логін вже зареестрованний.")
#                 return render(request, self.template_name, {'form': form})
#
#             if self.register_new_user(login, email, password):
#                 messages.success(request, "Ви успішно зареєструвалися!")
#                 return redirect(self.success_url)
#             else:
#                 messages.success(request, "Відбулася помилка! Спробуйте пізніше!")
#                 return redirect(self.success_url)
#
#         return render(request, self.template_name, {'form': form})
#
#     def register_new_user(self, login, email, password):
#         try:
#             user = User.objects.create_user(username=login, email=email, password=password)
#             user.save()
#             return True
#         except Exception as ex:
#             print(ex)
#             return False


# def login(request):
#     return render(request, 'user/login.html')

# def registration(request):
#     return render(request, 'user/register.html')

class ProfileView(DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'


class LogoutView(LogoutView):
    next_page = '/'
