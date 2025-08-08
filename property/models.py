from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

BUILDING_CONDITION = (
    (True, "Да"),
    (False, "Нет"),
    (None, "Неизвестно"),
)


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)
    owner_pure_phone = PhoneNumberField(verbose_name="Нормализированный номер владельца",blank=True,
            null=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    new_building = models.BooleanField('Новостройка', default=None, null=True, blank=True, choices=BUILDING_CONDITION)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    like_by = models.ManyToManyField(User, related_name="likes", verbose_name="Кто лайкнул", blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Plaint(models.Model):
    who_complained = models.ForeignKey(User, verbose_name='Кто жаловался', on_delete=models.CASCADE, related_name='complaints')
    apartment = models.ForeignKey(Flat, verbose_name='На какую квартиру жаловались', on_delete=models.CASCADE)
    text_complaint = models.TextField(verbose_name='Текст Жалобы')
    created_at = models.DateTimeField(auto_now_add=True)


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    phone = models.CharField('Номер владельца', max_length=20)
    pure_phone = PhoneNumberField(verbose_name="Нормализированный номер владельца", blank=True,
                                        null=True)
    flats = models.ManyToManyField("Flat", related_name="owners", verbose_name='Квартиры в собственности', blank=True)

    def __str__(self):
        return self.name

