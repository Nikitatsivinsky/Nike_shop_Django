from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from .forms import UserRegistrationForm, UserProfileForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.views.generic.edit import FormMixin

# photo
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

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

class ProfileView(FormMixin, DetailView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    context_object_name = 'user'
    success_url = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            for field_name, field_value in form.cleaned_data.items():
                if not field_value == '' and field_value is not None:
                    if hasattr(self.object, field_name):
                        if field_name == 'photo':
                            self.object.photo = self.formatting_photo_profile(field_value)
                            self.object.save()
                        else:
                            setattr(self.object, field_name, field_value)
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def formatting_photo_profile(self, photo):

        img = Image.open(photo)

        width, height = img.size
        size = min(width, height)
        left = (width - size) // 2
        top = (height - size) // 2
        right = left + size
        bottom = top + size
        img = img.crop((left, top, right, bottom))
        img = img.resize((150, 150), Image.ANTIALIAS)

        # Создать временный поток для сохранения измененного изображения
        temp_stream = io.BytesIO()
        img.save(temp_stream, format='JPEG')
        temp_stream.seek(0)

        # Создать InMemoryUploadedFile на основе данных из потока
        temp_file = InMemoryUploadedFile(
            temp_stream,
            None,
            photo.name,
            'image/jpeg',
            temp_stream.tell(),
            None
        )

        return temp_file

    def get_success_url(self):
        return self.request.get_full_path()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ChangePasswordView(PasswordChangeView):
    template_name = 'user/password.html'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        messages.success(self.request, 'Пароль успешно изменен.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_invalid(self, form):
        for errors in form.errors.items():
            for error_message in errors[1]:
                messages.error(self.request, error_message)
        return super().form_invalid(form)


class LogoutView(LogoutView):
    next_page = '/'
