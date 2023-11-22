# Generated by Django 4.2.7 on 2023-11-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
    ]
