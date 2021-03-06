# Generated by Django 3.0.3 on 2020-05-15 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_account', models.CharField(max_length=100)),
                ('from_account', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('card', models.BigIntegerField(validators=[django.core.validators.MinLengthValidator(12)])),
                ('bank', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('txntype', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('txnstatus', models.BooleanField(default=False)),
            ],
        ),
    ]
