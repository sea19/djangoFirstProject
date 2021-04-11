from django.contrib import admin
from . import models


@admin.register(models.HaircutModel)
class HaircutAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClientModel)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WorkModel)
class WorkAdmin(admin.ModelAdmin):
    pass
