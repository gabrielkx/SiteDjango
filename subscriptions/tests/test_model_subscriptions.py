from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Gabriel Oliveira",
            cpf=" 12345678901",
            email="seucarlinhos6@gmail.com",
            phone="5312345678",
        )
        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

        # subscription must have an auto create at attr.
    def tes_created_at(self):
        self.assertIsIstance(self.obj.created_at,datetime)