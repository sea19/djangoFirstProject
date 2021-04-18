from django.contrib import admin
from . import models


@admin.register(models.HaircutModel)
class HaircutAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'price')
    search_fields = ('name', 'gender', 'price')
    list_filter = ('gender',)


@admin.register(models.ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'phone', 'email', 'status')
    search_fields = ('last_name', 'first_name', 'patronymic', 'phone', 'email')
    list_filter = ('status',)


@admin.register(models.WorkModel)
class WorkAdmin(admin.ModelAdmin):
    fieldsets = (None, {'fields': ('haircut', 'client', 'master', 'date_time')}),
    list_display = ('date_time', 'haircut', 'client', 'master', 'final_cost')
    search_fields = ('date_time', 'haircut__name', 'client__last_name', 'client__first_name', 'client__patronymic',
                     'master__username', 'master__last_name', 'master__first_name', 'master__patronymic', 'final_cost')
