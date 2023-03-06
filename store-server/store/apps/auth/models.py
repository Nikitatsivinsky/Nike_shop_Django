from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логін', editable=False)
    telephone = models.CharField(max_length=20, verbose_name='Телефон', help_text='Формат телефону (xxx) xxx-xxxx',
                                 null=True, blank=True)
    country = models.CharField(max_length=20, verbose_name='Країна', null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name='Місто', null=True, blank=True)
    adress = models.CharField(max_length=20, verbose_name='Адреса', null=True, blank=True)
    zip_code = models.CharField(max_length=20, verbose_name='Індекс', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата народження')
    photo = models.ImageField(upload_to='profile_image/', verbose_name='Фото', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'
        app_label = 'auth'
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
