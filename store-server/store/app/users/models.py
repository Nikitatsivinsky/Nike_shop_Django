from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    telephone = models.CharField(max_length=20, verbose_name='Телефон', help_text='Формат телефону (xxx) xxx-xxxx',
                                 null=True, blank=True)
    country = models.CharField(max_length=20, verbose_name='Країна', null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name='Місто', null=True, blank=True)
    address = models.CharField(max_length=20, verbose_name='Адреса', null=True, blank=True)
    zip_code = models.CharField(max_length=20, verbose_name='Індекс', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата народження')
    photo = models.ImageField(upload_to='users_image/', verbose_name='Фото', null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        app_label = 'custom_user'


class MailDistribution(models.Model):
    email = models.EmailField(max_length=50, verbose_name='Пошта', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'maildistribution'
        verbose_name = 'Пошта розсилання'
        verbose_name_plural = 'Пошта розсилання'