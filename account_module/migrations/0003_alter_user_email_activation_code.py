# Generated by Django 4.0.6 on 2022-12-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_alter_user_email_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_activation_code',
            field=models.CharField(max_length=100, verbose_name='کد فعال سازی'),
        ),
    ]
