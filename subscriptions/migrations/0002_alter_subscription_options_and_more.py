# Generated by Django 4.0.2 on 2022-03-13 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Inscrição', 'verbose_name_plural': 'Inscrições'},
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
