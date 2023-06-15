from django.db import models
from apps.shop.models import Item
from django.conf import settings
from django.core.exceptions import ValidationError

class MainBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Головний банер на головній сторінці'
        verbose_name_plural = 'Головний банер на головній сторінці'
        # app_label = 'other'
        db_table = 'main_banner'


class NewesBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    def save(self, *args, **kwargs):
        if NewesBanner.objects.count() >= settings.MAX_BANNER_COUNT:
            raise ValidationError("Перевищено ліміт кількості об'єктів моделі Банеру 'Новинки магазину'")
        super(NewesBanner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банер "Новинки магазину" на головній сторінці'
        verbose_name_plural = 'Банер "Новинки магазину" на головній сторінці'
        # app_label = 'other'
        db_table = 'newes_banner'


class SaleBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    def save(self, *args, **kwargs):
        if SaleBanner.objects.count() >= settings.MAX_BANNER_COUNT:
            raise ValidationError("Перевищено ліміт кількості об'єктів моделі Банеру 'Розпродаж'")
        super(SaleBanner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банер "Розпродаж" на головній сторінці'
        verbose_name_plural = 'Банер "Розпродаж" на головній сторінці'
        # app_label = 'other'
        db_table = 'sale_banner'


class ExclusiveBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Банер "Єксклюзивні товари" на головній сторінці'
        verbose_name_plural = 'Банер "Єксклюзивні товари" на головній сторінці'
        # app_label = 'other'
        db_table = 'exclusive_banner'


class PopularBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    def save(self, *args, **kwargs):
        if PopularBanner.objects.count() >= settings.MAX_POPULAR_BANNER_COUNT:
            raise ValidationError("Перевищено ліміт кількості об'єктів моделі Банеру 'Популярні товари'")
        super(PopularBanner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банер "Популярні товари"'
        verbose_name_plural = 'Банер "Популярні товари"'
        # app_label = 'other'
        db_table = 'popular_banner'
