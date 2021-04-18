from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import HaircutModel, ClientModel, WorkModel
from mainApp import admin
from datetime import datetime
from decimal import Decimal

User = get_user_model()


class HairdressingSalon(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='qweasd123456789')
        self.haircut = HaircutModel.objects.create(name='Тестовая прическа', gender='f', price=2300)
        self.client = ClientModel.objects.create(last_name='Иванов', first_name='Иван', patronymic='Иванович',
                                                 phone='89123459745', status=False)

    def test_update_haircut(self):
        self.haircut.name = 'Новая тестовая прическа'
        self.assertEqual(self.haircut.name, 'Новая тестовая прическа')

    def test_add_work(self):
        self.work = WorkModel.objects.create(haircut=self.haircut, client=self.client, master=self.user,
                                             date_time=datetime.now())

    def test_change_client_status(self):
        self.assertEqual(self.client.status, False)
        self.assertEqual(WorkModel.objects.filter(client=self.client).count(), 0)
        while WorkModel.objects.filter(client=self.client).count() <= 4:
            self.test_add_work()
        self.assertEqual(self.client.status, False)
        self.assertEqual(self.work.final_cost, Decimal('2300.00'))
        self.test_add_work()
        self.assertEqual(self.client.status, True)
        self.assertEqual(self.work.final_cost, Decimal('2231.00'))
