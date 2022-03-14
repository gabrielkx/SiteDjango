from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Seu Carlinhos',
                    cpf='21-99618-6180',
                    email='seucarlinhos6@gmail.com',
                    phone='21-099345-23554')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscriptioin_from(self):
        expect = 'seucarlinhos6@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['seucarlinhos6@gmail.com',
                  'seucarlinhos6@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Seu Carlinhos',
                    '21-99618-6180',
                    'seucarlinhos6@gmail.com',
                    '21-099345-23554'
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)