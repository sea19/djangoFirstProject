# Generated by Django 3.2 on 2021-04-18 15:17

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('status', models.BooleanField(verbose_name='Постоянный клиент')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='HaircutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название стрижки')),
                ('gender', models.CharField(choices=[('f', 'женская'), ('m', 'мужская')], max_length=1, verbose_name='Пол')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Стрижка',
                'verbose_name_plural': 'Стрижки',
            },
        ),
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Дата и время')),
                ('final_cost', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая стоимость')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainApp.clientmodel', verbose_name='Клиент')),
                ('haircut', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainApp.haircutmodel', verbose_name='Стрижка')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
    ]
