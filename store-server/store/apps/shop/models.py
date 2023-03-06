from django.db import models
import uuid


class Application(models.Model):
    name = models.CharField(max_length=50, verbose_name='Застосування')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'application'
        verbose_name = 'Застосування'
        verbose_name_plural = 'Застосування'


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Виробник')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
        verbose_name = 'Виробника'
        verbose_name_plural = 'Виробники'


class Category(models.Model):
    name = models.CharField(null=False, max_length=50, verbose_name='Категорія')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class SubCategory(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Cуб-Категорія')
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категорія')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Cуб-Категорія'
        verbose_name_plural = 'Cуб-Категорії'


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Колір')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'color'
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'


class Gender(models.Model):
    name = models.CharField(max_length=30, verbose_name='Стать')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gender'
        verbose_name = 'Стать'
        verbose_name_plural = 'Стать'


class Material(models.Model):
    name = models.CharField(max_length=50, verbose_name='Матеріал')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'material'
        verbose_name = 'Матеріал'
        verbose_name_plural = 'Матеріали'


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типи'


class Size(models.Model):
    name = models.DecimalField(max_digits=3, decimal_places=1, unique=True, verbose_name='Розмір')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'size'
        verbose_name = 'Розмір'
        verbose_name_plural = 'Розміри'


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name='Назва товару')
    model = models.CharField(max_length=50, verbose_name='Модель товару', null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Виробник')
    applications = models.ManyToManyField('Application', verbose_name='Застосування')
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, verbose_name='Категорія')
    subcategory = models.ManyToManyField('SubCategory', verbose_name='Cуб-Категорія')
    colors = models.ManyToManyField('Color', verbose_name='Колір')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Стать')
    materials = models.ManyToManyField('Material', verbose_name='Матеріал')
    types = models.ManyToManyField('Type', verbose_name='Тип')
    image = models.ImageField(upload_to='product_image/', verbose_name='Фото')
    description = models.TextField(verbose_name='Опис')
    famous = models.IntegerField(verbose_name='Популярність')
    in_stock = models.IntegerField(verbose_name='На складі')
    length_cm = models.IntegerField(null=True, blank=True, verbose_name='Довжина')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    size = models.ManyToManyField('Size', verbose_name='Розміри')
    weight = models.IntegerField(verbose_name='Вага')
    year = models.IntegerField(null=True, blank=True, verbose_name='Рік')

    def __str__(self):
        return str(f'{self.name} {self.model}')

    class Meta:
        db_table = 'item'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class MainBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Головний банер на головній сторінці'
        verbose_name_plural = 'Головний банер на головній сторінці'
        app_label = 'other'
        db_table = 'main_banner'


class NewesBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Банер "Новинки магазину" на головній сторінці'
        verbose_name_plural = 'Банер "Новинки магазину" на головній сторінці'
        app_label = 'other'
        db_table = 'newes_banner'


class SaleBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Банер "Розпродаж" на головній сторінці'
        verbose_name_plural = 'Банер "Розпродаж" на головній сторінці'
        app_label = 'other'
        db_table = 'sale_banner'


class ExclusiveBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Банер "Єксклюзивні товари" на головній сторінці'
        verbose_name_plural = 'Банер "Єксклюзивні товари" на головній сторінці'
        app_label = 'other'
        db_table = 'exclusive_banner'


class PopularBanner(models.Model):
    subject = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Назва товару')

    def __str__(self):
        return str(self.subject)

    class Meta:
        verbose_name = 'Банер "Популярні товари"'
        verbose_name_plural = 'Банер "Популярні товари"'
        app_label = 'other'
        db_table = 'popular_banner'
