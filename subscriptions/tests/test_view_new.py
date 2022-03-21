from django.core import mail
from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r

class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:new'))

    def test_get(self):
        #"""GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        #"""Must return subscriptions/subscription_form.html"""
        response = self.client.get(r('subscriptions:new'))
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        #"""html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1)
                )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        #"html mst contaian csrf"
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_form_has_fields(self):
        #""""Form must have 4 fields"""
        form = self.resp.context["form"]
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Seu carlinhos',
                    cpf='21996186180',
                    email='seucarlinhos6@gmail.com',
                    phone='21099345-23554')
        self.resp = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        #"""Valid POST redirect to  /inscricao/"""
        self.assertRedirects(self.resp, r('subscriptions:detail',1))

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscriptions(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:new'))

    def test_post(self):
        #""""Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscriptions(self):
        self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')