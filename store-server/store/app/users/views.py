from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from .forms import UserRegistrationForm, UserProfileForm, ChangePasswordForm, UserLoginForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormMixin

# photo
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
# Confirm email
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import redirect, get_object_or_404
# Reset password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# user session remember_me
from django.contrib.sessions.backends.db import SessionStore

User = get_user_model()


# Create your views here.
def checkout(request):
    return render(request, 'user/checkout.html')

def login_redirect(request):
    return redirect('login')

def confirm_email(request, user_id):
    user = get_object_or_404(User, id=user_id)

    user.is_email_confirmed = True
    user.save()

    return redirect(f'/')

from django.contrib.auth.hashers import check_password
class MyLoginView(LoginView):
    template_name = 'user/register.html'
    redirect_authenticated_user = False
    next_page = '/'
    form_class = UserLoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        remember_me = self.request.POST.get('remember_me', False)

        # Аутентификация пользователя по имени пользователя или адресу электронной почты и паролю
        user = authenticate(username=username, password=password)

        if user is not None:

            if not user.is_email_confirmed:
                messages.error(self.request, "Пожалуйста, подтвердите свою почту для авторизации.")
                return self.form_invalid(form)

            if remember_me == 'on':
                session = SessionStore()
                session.set_expiry(None)
                user.remember_me = True
                user.save()
                self.request.session = session
            else:
                if 'remember_me' in self.request.session:
                    del self.request.session['remember_me']
                    self.request.session.modified = True

            login(self.request, user)
            return super().form_valid(form)

        # Если пользователь не найден, отобразить ошибку
        messages.error(self.request, "Неверное имя пользователя, адрес электронной почты или пароль.")
        return super().form_invalid(form)

    def form_invalid(self, form):

        for errors in form.errors.items():
            for error_message in errors[1]:
                messages.error(self.request, error_message)
        return super().form_invalid(form)

# class MyLoginView(LoginView):
#     template_name = 'user/register.html'
#     redirect_authenticated_user = False
#     next_page = '/'


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
        # password2 = form.data['password2']
        email = form.data['email']
        username = form.cleaned_data['username']

        email_in_db = User.objects.filter(email=email).exists()
        login_in_db = User.objects.filter(username=username).exists()

        if email_in_db:
            messages.error(self.request, "Ця пошта вже зареестрованна.")
            return self.form_invalid(form)
        elif login_in_db:
            messages.error(self.request, "Цей логін вже зареестрованний.")
            return self.form_invalid(form)

        if self.register_new_user(username, email, password1):
            self.send_confirmation_email()
            messages.success(self.request, "Ви успішно зареєструвалися! Перевірте свою поштову скриньку для підтвердження реєстрації.")
            return render(self.request, 'user/popup_template.html', {
                'message': 'Ви успішно зареєструвалися! Перевірте свою поштову скриньку для підтвердження реєстрації.'})
        else:
            messages.success(self.request, "Відбулася помилка! Спробуйте пізніше!")
        return super().form_valid(form)

    def register_new_user(self, username, email, password):
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            self.user = user
            return True
        except Exception as ex:
            print(ex)
            return False

    def send_confirmation_email(self):
        current_site = get_current_site(self.request)
        mail_subject = 'Подтверждение регистрации'

        # Генерация ссылки для подтверждения
        confirmation_link = f"http://{current_site.domain}/user/confirm/{self.user.id}/"

        html_message = render_to_string('user/confirmation_email.html', {
            'user': self.user,
            'confirmation_link': confirmation_link,
        })
        text_message = strip_tags(html_message)  # Преобразование HTML в текст

        # Создание EmailMultiAlternatives объекта
        email = EmailMultiAlternatives(
            mail_subject, text_message, to=[self.user.email]
        )
        email.attach_alternative(html_message, "text/html")  # Добавление HTML версии письма

        # Отправка сообщения
        email.send()


        # # Загрузка шаблона электронного сообщения
        # message = render_to_string('user/confirmation_email.html', {
        #     'user': self.user,
        #     'confirmation_link': confirmation_link,
        # })
        #
        # # Отправка сообщения
        # email = EmailMessage(
        #     mail_subject, message, to=[self.user.email]
        # )
        # email.send()


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


class MyPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user/password_reset_complete.html'

class MyLogoutView(LogoutView):
    next_page = '/'
