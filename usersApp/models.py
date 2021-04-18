from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group


class CustomUser(AbstractUser):
    patronymic = models.CharField(_('Отчество'), null=True, max_length=150, blank=True)
    phone = PhoneNumberField(_('Телефон'), null=True, blank=True)


class CustomGroup(Group):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
