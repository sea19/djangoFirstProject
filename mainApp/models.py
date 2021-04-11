from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class HaircutModel(models.Model):
    CHECKLIST_OPTIONS = (
        (True, 'женская'),
        (False, 'мужская'),
    )

    name = models.CharField(null=False, max_length=256, verbose_name='Название стрижки')
    gender = models.BooleanField(null=False, choices=CHECKLIST_OPTIONS, verbose_name='Пол')
    price = models.DecimalField(null=False, max_digits=9, decimal_places=2, verbose_name='Цена')

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
                                 self.patronymic if self.patronymic is not None else '')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class WorkModel(models.Model):

    haircut = models.ForeignKey('HaircutModel', null=True, verbose_name='Стрижка', on_delete=models.DO_NOTHING)
    client = models.ForeignKey('ClientModel', null=True, verbose_name='Клиент', on_delete=models.DO_NOTHING)
    master = models.ForeignKey(User, null=True, verbose_name='Мастер', on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(null=True, verbose_name='Дата и время')

    def __str__(self):
        return 'Стрижка: {}, клиент: {} {} {}, мастер: {} {}, дата и время: {}'\
            .format(self.haircut.name, self.client.last_name, self.client.first_name,
                    self.client.patronymic if self.client.patronymic is not None else '', self.master.last_name,
                    self.master.first_name, self.date_time)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
