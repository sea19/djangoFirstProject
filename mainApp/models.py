from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

User = get_user_model()


class HaircutModel(models.Model):
    CHECKLIST_OPTIONS = (
        ('f', 'женская'),
        ('m', 'мужская'),
    )

    name = models.CharField(max_length=256, verbose_name='Название стрижки')
    gender = models.CharField(max_length=1, choices=CHECKLIST_OPTIONS, verbose_name='Пол')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Стрижки'


class ClientModel(models.Model):
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    patronymic = models.CharField(null=True, blank=True, max_length=256, verbose_name='Отчество')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(null=True, blank=True)
    status = models.BooleanField(verbose_name='Постоянный клиент')

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name,
                                 self.patronymic or '')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class WorkModel(models.Model):

    haircut = models.ForeignKey('HaircutModel', null=True, verbose_name='Стрижка', on_delete=models.DO_NOTHING)
    client = models.ForeignKey('ClientModel', null=True, verbose_name='Клиент', on_delete=models.DO_NOTHING)
    master = models.ForeignKey(User, null=True, verbose_name='Мастер', on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(verbose_name='Дата и время')
    final_cost = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Общая стоимость')

    def __str__(self):
        return 'Работа'

    def save(self):
        if self.client.status:
            self.final_cost = self.haircut.price-self.haircut.price*5/100
        else:
            self.final_cost = self.haircut.price
        super().save()

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
