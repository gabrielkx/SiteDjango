# Generated by Django 4.0.2 on 2022-03-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_alter_subscription_options_alter_subscription_cpf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]