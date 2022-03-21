from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Gabriel Oliveira',
                    cpf='21996186180',
                    email='seucarlinhos6@gmail.com',
                    phone='2109934523554')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_from(self):
        expect = 'seucarlinhos6@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['seucarlinhos6@gmail.com',
                  'seucarlinhos6@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Gabriel Oliveira',
                    '21996186180',
                    'seucarlinhos6@gmail.com',
                    '2109934523554'
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)